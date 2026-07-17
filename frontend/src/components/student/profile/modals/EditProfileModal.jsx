import { useState } from "react";
import { X } from "lucide-react";

import PersonalTab from "./tabs/PersonalTab";
import ContactTab from "./tabs/ContactTab";
import ParentTab from "./tabs/ParentTab";
import AcademicTab from "./tabs/AcademicTab";
import SocialTab from "./tabs/SocialTab";
import ResumeTab from "./tabs/ResumeTab";

export default function EditProfileModal({ student, onSave, onClose }) {
    const [activeTab, setActiveTab] = useState("personal");
    const [formData, setFormData] = useState(student);

    const handleSave = () => {
  console.log("Updated Profile", formData);

  // Update parent component
  onSave(formData);

  onClose();
};

    const tabs = {
  personal: (
    <PersonalTab
      formData={formData}
      setFormData={setFormData}
    />
  ),

  contact: (
    <ContactTab
      formData={formData}
      setFormData={setFormData}
    />
  ),

  parent: (
    <ParentTab
      formData={formData}
      setFormData={setFormData}
    />
  ),

  academic: (
    <AcademicTab
      formData={formData}
    />
  ),

  social: (
    <SocialTab
      formData={formData}
      setFormData={setFormData}
    />
  ),

  resume: (
    <ResumeTab
      formData={formData}
    />
  ),
};

    const navigationTabs = [
  { id: "personal", label: "Personal" },
  { id: "contact", label: "Contact" },
  { id: "parent", label: "Parent" },
  { id: "academic", label: "Academic" },
  { id: "social", label: "Social" },
  { id: "resume", label: "Resume" },
];

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="fixed inset-0 z-50 flex items-center justify-center p-6">
        <div className="w-full max-w-5xl rounded-3xl bg-white shadow-2xl">

          {/* Header */}
          <div className="flex items-center justify-between border-b px-8 py-6">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">
                Edit Profile
              </h2>

              <p className="mt-1 text-gray-500">
                Update your personal information.
              </p>
            </div>

            <button
              onClick={onClose}
              className="rounded-xl p-2 transition hover:bg-gray-100"
            >
              <X size={22} />
            </button>
          </div>

          <div className="border-b">
  <div className="flex gap-8 px-8">

    {navigationTabs.map((tab) => (
      <button
        key={tab.id}
        onClick={() => setActiveTab(tab.id)}
        className={`border-b-2 py-4 text-sm font-semibold capitalize transition
        ${
          activeTab === tab.id
            ? "border-[#8E1528] text-[#8E1528]"
            : "border-transparent text-gray-500 hover:text-gray-900"
        }`}
      >
        {tab.label}
      </button>
    ))}

  </div>
</div>

          {/* Body */}
          <div className="max-h-[70vh] overflow-y-auto px-8 py-8">
            
            <div className="max-h-[70vh] overflow-y-auto px-8 py-8">
              {tabs[activeTab]}
            </div>

          </div>

          {/* Footer */}
          <div className="flex justify-end gap-4 border-t px-8 py-5">

            <button
              onClick={onClose}
              className="rounded-xl border border-gray-300 px-6 py-3 font-medium hover:bg-gray-50"
            >
              Cancel
            </button>

            <button
              onClick={handleSave}
              className="rounded-xl bg-[#8E1528] px-6 py-3 font-medium text-white hover:bg-[#73111f]"
            >
              Save Changes
            </button>

          </div>

        </div>
      </div>
    </>
  );
}