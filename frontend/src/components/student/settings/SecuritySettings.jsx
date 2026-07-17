import { useState } from "react";

import ChangePasswordModal from "./ChangePasswordModal";
import ActiveSessionsModal from "./ActiveSessionsModal";

import {
  FiLock,
  FiShield,
  FiMonitor,
  FiLogOut,
  FiTrash2,
} from "react-icons/fi";

export default function SecuritySettings() {
  const [isPasswordOpen, setIsPasswordOpen] = useState(false);
  const [isSessionsOpen, setIsSessionsOpen] = useState(false);

  return (
    <>
    <section className="rounded-2xl border border-gray-200 bg-white">

      {/* Header */}

      <div className="border-b px-8 py-6">

        <h2 className="text-2xl font-bold">
          Security
        </h2>

        <p className="mt-1 text-gray-500">
          Manage your account security and login sessions.
        </p>

      </div>

      {/* Change Password */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiLock className="text-2xl text-[#8E1528]" />

          <div>

            <h3 className="font-semibold">
              Change Password
            </h3>

            <p className="text-sm text-gray-500">
              Update your account password.
            </p>

          </div>

        </div>

        <button
  onClick={() => setIsPasswordOpen(true)}
  className="rounded-xl border border-gray-300 px-5 py-2 hover:bg-gray-50"
>
  Change
</button>

      </div>

      {/* 2FA */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiShield className="text-2xl text-green-600" />

          <div>

            <h3 className="font-semibold">
              Two-Factor Authentication
            </h3>

            <p className="text-sm text-gray-500">
              Add an extra layer of security.
            </p>

          </div>

        </div>

        <button className="rounded-xl border border-gray-300 px-5 py-2 hover:bg-gray-50">
          Enable
        </button>

      </div>

      {/* Active Sessions */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiMonitor className="text-2xl text-blue-600" />

          <div>

            <h3 className="font-semibold">
              Active Sessions
            </h3>

            <p className="text-sm text-gray-500">
              Windows • Chrome • Mumbai
            </p>

          </div>

        </div>

        <button
  onClick={() => setIsSessionsOpen(true)}
  className="rounded-xl border border-gray-300 px-5 py-2 hover:bg-gray-50"
>
  View
</button>

      </div>

      {/* Logout */}

      <div className="flex items-center justify-between border-b border-gray-100 px-8 py-5">

        <div className="flex items-center gap-4">

          <FiLogOut className="text-2xl text-orange-600" />

          <div>

            <h3 className="font-semibold">
              Logout All Devices
            </h3>

            <p className="text-sm text-gray-500">
              Sign out from every device.
            </p>

          </div>

        </div>

        <button className="rounded-xl bg-orange-500 px-5 py-2 text-white hover:bg-orange-600">
          Logout
        </button>

      </div>

      {/* Delete */}

      <div className="flex items-center justify-between px-8 py-5">

        <div className="flex items-center gap-4">

          <FiTrash2 className="text-2xl text-red-600" />

          <div>

            <h3 className="font-semibold text-red-600">
              Delete Account
            </h3>

            <p className="text-sm text-gray-500">
              Permanently request account deletion.
            </p>

          </div>

        </div>

        <button className="rounded-xl bg-red-600 px-5 py-2 text-white hover:bg-red-700">
          Request
        </button>

      </div>

    </section>

<ChangePasswordModal
  isOpen={isPasswordOpen}
  onClose={() => setIsPasswordOpen(false)}/>

  <ActiveSessionsModal
  isOpen={isSessionsOpen}
  onClose={() => setIsSessionsOpen(false)}/>


</>
);
}