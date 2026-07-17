import { useState } from "react";
import {
  FiX,
  FiEye,
  FiEyeOff,
  FiLock,
} from "react-icons/fi";

export default function ChangePasswordModal({
  isOpen,
  onClose,
}) {
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [showCurrent, setShowCurrent] = useState(false);
  const [showNew, setShowNew] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  if (!isOpen) return null;

  const passwordStrength = () => {
    let score = 0;

    if (newPassword.length >= 8) score++;
    if (/[A-Z]/.test(newPassword)) score++;
    if (/[0-9]/.test(newPassword)) score++;
    if (/[^A-Za-z0-9]/.test(newPassword)) score++;

    return score;
  };

  const strength = passwordStrength();

  const colors = [
    "bg-gray-200",
    "bg-red-500",
    "bg-orange-500",
    "bg-yellow-500",
    "bg-green-600",
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center overflow-y-auto bg-black/40 p-6">

      <div className="my-8 w-full max-w-xl rounded-2xl bg-white shadow-2xl max-h-[90vh] overflow-y-auto">

        <div className="flex items-center justify-between border-b px-6 py-5">

          <div className="flex items-center gap-3">

            <FiLock className="text-2xl text-[#8E1528]" />

            <h2 className="text-2xl font-bold">
              Change Password
            </h2>

          </div>

          <button
            onClick={onClose}
            className="rounded-lg p-2 hover:bg-gray-100"
          >
            <FiX />
          </button>

        </div>

        <div className="space-y-5 p-6">

          {/* Current Password */}

          <PasswordInput
            label="Current Password"
            value={currentPassword}
            setValue={setCurrentPassword}
            show={showCurrent}
            setShow={setShowCurrent}
          />

          {/* New Password */}

          <PasswordInput
            label="New Password"
            value={newPassword}
            setValue={setNewPassword}
            show={showNew}
            setShow={setShowNew}
          />

          {/* Confirm */}

          <PasswordInput
            label="Confirm Password"
            value={confirmPassword}
            setValue={setConfirmPassword}
            show={showConfirm}
            setShow={setShowConfirm}
          />

          <div>

            <div className="mb-2 flex gap-2">

              {[1,2,3,4].map((item)=>(
                <div
                  key={item}
                  className={`h-2 flex-1 rounded ${
                    strength >= item
                      ? colors[strength]
                      : "bg-gray-200"
                  }`}
                />
              ))}

            </div>

            <p className="text-sm text-gray-500">
              Password Strength
            </p>

          </div>

          <div className="rounded-xl bg-gray-50 p-4">

            <h3 className="mb-3 font-semibold">
              Password Requirements
            </h3>

            <ul className="space-y-2 text-sm">

              <li>
                {newPassword.length >= 8 ? "✅" : "⬜"} Minimum 8 characters
              </li>

              <li>
                {/[A-Z]/.test(newPassword) ? "✅" : "⬜"} One uppercase letter
              </li>

              <li>
                {/[0-9]/.test(newPassword) ? "✅" : "⬜"} One number
              </li>

              <li>
                {/[^A-Za-z0-9]/.test(newPassword) ? "✅" : "⬜"} One special character
              </li>

              <li>
                {confirmPassword &&
                confirmPassword === newPassword
                  ? "✅"
                  : "⬜"} Passwords match
              </li>

            </ul>

          </div>

        </div>

        <div className="flex justify-end gap-3 border-t px-6 py-5">

          <button
            onClick={onClose}
            className="rounded-xl border px-5 py-2 hover:bg-gray-100"
          >
            Cancel
          </button>

          <button
            className="rounded-xl bg-[#8E1528] px-5 py-2 text-white hover:bg-[#731120]"
          >
            Update Password
          </button>

        </div>

      </div>

    </div>
  );
}

function PasswordInput({
  label,
  value,
  setValue,
  show,
  setShow,
}) {
  return (
    <div>

      <label className="mb-2 block font-medium">
        {label}
      </label>

      <div className="relative">

        <input
          type={show ? "text" : "password"}
          value={value}
          onChange={(e)=>setValue(e.target.value)}
          className="w-full rounded-xl border p-3 pr-12"
        />

        <button
          type="button"
          onClick={()=>setShow(!show)}
          className="absolute right-3 top-3"
        >
          {show ? <FiEyeOff /> : <FiEye />}
        </button>

      </div>

    </div>
  );
}