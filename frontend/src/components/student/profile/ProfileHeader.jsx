import {
  User,
  GraduationCap,
  Calendar,
  Pencil,
  Mail,
  BadgeCheck,
  Briefcase,
} from "lucide-react";

export default function ProfileHeader({
  student,
  onEditProfile,
}) {
  return (
    <div className="overflow-hidden rounded-3xl bg-white shadow">

      {/* Banner */}

      <div className="h-44 bg-gradient-to-r from-[#8E1528] to-[#b21f3a]" />

      <div className="relative px-10 pb-8">

        {/* Profile Image */}

        <div className="-mt-20 flex flex-wrap items-end justify-between gap-8">

          <div className="flex gap-6">

            <div className="flex h-30 w-30 items-center justify-center rounded-full border-8 border-white bg-gray-100 shadow-xl">
              <User size={90} className="text-gray-400" />
            </div>

            <div className="pt-8">

              <h1 className="text-3xl font-bold text-gray-900">
                {student.fullName}
              </h1>

              <p className="mt-2 text-lg font-medium text-gray-700">
                {student.rollNo}
              </p>

              <p className="text-gray-500">
                {student.program}
              </p>

              <p className="text-sm text-gray-400">
                Department of {student.department}
              </p>

              <div className="mt-5 flex flex-wrap gap-3">

                <span className="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700">
                  Semester {student.semester}
                </span>

                <span className="rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">
                  CGPA {student.cgpa}
                </span>

                <span className="flex items-center gap-2 rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">
                  <BadgeCheck size={18} />
                  Verified Student
                </span>

                <span className="flex items-center gap-2 rounded-full bg-yellow-100 px-4 py-2 text-sm font-semibold text-yellow-700">
                  <Briefcase size={18} />
                  Placement Eligible
                </span>

              </div>

            </div>

          </div>

          <button
            onClick={onEditProfile}
            className="flex items-center gap-2 rounded-xl bg-[#8E1528] px-6 py-3 text-white transition hover:bg-[#73111f]"
          >
            <Pencil size={18} />
            Edit Profile
          </button>

        </div>

        {/* Quick Info */}

        <div className="mt-10 grid grid-cols-1 gap-5 md:grid-cols-3">

          <div className="flex items-center gap-4 rounded-2xl border p-5">

            <Mail className="text-[#8E1528]" />

            <div>
              <p className="text-gray-500">Email</p>
              <p className="font-semibold">{student.email}</p>
            </div>

          </div>

          <div className="flex items-center gap-4 rounded-2xl border p-5">

            <GraduationCap className="text-[#8E1528]" />

            <div>
              <p className="text-gray-500">Department</p>
              <p className="font-semibold">{student.department}</p>
            </div>

          </div>

          <div className="flex items-center gap-4 rounded-2xl border p-5">

            <Calendar className="text-[#8E1528]" />

            <div>
              <p className="text-gray-500">Academic Year</p>
              <p className="font-semibold">
                {student.academicYear}
              </p>
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}