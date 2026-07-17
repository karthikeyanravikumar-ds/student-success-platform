import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../services/authService";
import { getCurrentUser } from "../../services/userService";
import { getMyProfile } from "../../services/studentService";
import whiteLogo from "../../assets/images/white-vsit-logo.png";

export default function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleLogin = async (e) => {
        console.log("NEW LOGIN CODE IS RUNNING");
  e.preventDefault();

  setError("");
  setLoading(true);

  try {
    const data = await login(email, password);

    localStorage.setItem("access_token", data.access_token);

    const currentUser = await getCurrentUser();

    console.log("Current User:", currentUser);

    if (currentUser.role === "Student") {
        const student = await getMyProfile();

        console.log("Student Profile:", student);
    }

    navigate("/student");

  } catch (err) {
    console.error(err);

      if (err.response) {
    console.log("Status:", err.response.status);
    console.log("Data:", err.response.data);
  }

    setError("Invalid email or password.");

  } finally {
    setLoading(false);
  }
  };
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">

      <div className="w-full max-w-md rounded-2xl bg-white shadow-xl">

        {/* Top */}

        <div className="rounded-t-2xl bg-[#8E1528] p-8 text-center">

          <img
            src={whiteLogo}
            alt="VSIT"
            className="mx-auto h-16"
          />

          <h1 className="mt-6 text-2xl font-bold text-white">
            Student Success Platform
          </h1>

          <p className="mt-2 text-sm text-red-100">
            Vidyalankar School of Information Technology
          </p>

        </div>

        {/* Body */}

        <form
        onSubmit={handleLogin}
        className="space-y-5 p-8"
        >

          <div>

            <label className="mb-2 block text-sm font-semibold text-gray-700">
              VSIT Email
            </label>

            <input
              type="email"
              placeholder="student@vsit.edu.in"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-lg border border-gray-300 px-4 py-3 outline-none focus:border-[#8E1528]"
            />

          </div>

          <div>

            <label className="mb-2 block text-sm font-semibold text-gray-700">
              Password
            </label>

            <input
              type="password"
              placeholder="Enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-lg border border-gray-300 px-4 py-3 outline-none focus:border-[#8E1528]"
            />

          </div>

          {error && (
            <p className="rounded-md bg-red-100 p-3 text-sm text-red-700">
                {error}
            </p>
          )}

          <button
          type="submit"
          disabled={loading}
          className="w-full rounded-lg bg-[#8E1528] py-3 font-semibold text-white transition hover:bg-[#73111f] disabled:opacity-50"
          >
            {loading ? "Signing In..." : "Sign In"}
          </button>

        </form>

        {/* Footer */}

        <div className="border-t px-8 py-4 text-center text-sm text-gray-500">
          © 2026 Vidyalankar School of Information Technology
        </div>

      </div>

    </div>
  );
}