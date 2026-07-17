import { useRef, useState } from "react";
import {
  FiUser,
  FiMail,
  FiPhone,
  FiBook,
  FiHash,
  FiCamera,
  FiEdit,
} from "react-icons/fi";

import EditProfileModal from "./EditProfileModal";

export default function ProfileSettings() {
  const [student, setStudent] = useState({
    name: "Angel",
    roll: "24315A0036",
    email: "angel@vsit.edu.in",
    phone: "+91 9876543210",
    department: "B.Sc Data Science",
  });

  const fileInputRef = useRef(null);

  const [isEditOpen, setIsEditOpen] = useState(false);
  const [profileImage, setProfileImage] = useState(null);

  const rows = [
    {
      icon: <FiHash className="text-[#8E1528] text-xl" />,
      label: "Roll Number",
      value: student.roll,
    },
    {
      icon: <FiMail className="text-[#8E1528] text-xl" />,
      label: "Email",
      value: student.email,
    },
    {
      icon: <FiPhone className="text-[#8E1528] text-xl" />,
      label: "Phone",
      value: student.phone,
    },
    {
      icon: <FiBook className="text-[#8E1528] text-xl" />,
      label: "Department",
      value: student.department,
    },
  ];

  const handleImageChange = (event) => {
  const file = event.target.files[0];

  if (!file) return;

  const imageUrl = URL.createObjectURL(file);

  setProfileImage(imageUrl);
};

  return (
    <>
    <section className="rounded-2xl border border-gray-200 bg-white">

      {/* Header */}

      <div className="border-b px-8 py-8">

        <div className="flex items-center justify-between">

          <div className="flex items-center gap-6">

            <div className="h-24 w-24 overflow-hidden rounded-full bg-[#8E1528]">

  {profileImage ? (

    <img
      src={profileImage}
      alt="Profile"
      className="h-full w-full object-cover"
    />

  ) : (

    <div className="flex h-full w-full items-center justify-center text-4xl text-white">
      <FiUser />
    </div>

  )}

</div>

            <div>

              <h2 className="text-2xl font-bold">
                {student.name}
              </h2>

              <p className="text-gray-500">
                Student Profile
              </p>

              <p className="mt-1 text-sm text-gray-500">
                {student.roll}
              </p>

            </div>

          </div>

          <div className="flex gap-3">

  <button
    onClick={() => fileInputRef.current.click()}
    className="flex items-center gap-2 rounded-xl border border-gray-300 px-5 py-2 hover:bg-gray-50"
  >
    <FiCamera />
    Change Photo
  </button>

  <input
    ref={fileInputRef}
    type="file"
    accept="image/*"
    hidden
    onChange={handleImageChange}
  />

  <button
    onClick={() => setIsEditOpen(true)}
    className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-5 py-2 text-white hover:bg-[#731120]"
  >
    <FiEdit />
    Edit Profile
  </button>

</div>

        </div>

      </div>

      {/* Details */}

      {rows.map((row, index) => (

        <div
          key={row.label}
          className={`flex items-center justify-between px-8 py-5 ${
            index !== rows.length - 1
              ? "border-b border-gray-100"
              : ""
          }`}
        >

          <div className="flex items-center gap-4">

            {row.icon}

            <div>

              <h3 className="font-semibold">
                {row.label}
              </h3>

              <p className="text-sm text-gray-500">
                {row.value}
              </p>

            </div>

          </div>

        </div>

      ))}

    </section>

    <EditProfileModal
  isOpen={isEditOpen}
  onClose={() => setIsEditOpen(false)}
  student={student}
  onSave={(updatedStudent) => {
    setStudent(updatedStudent);
  }}
/>
    </>
  );
}