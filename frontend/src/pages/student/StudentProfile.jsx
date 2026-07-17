import { useState } from "react";

import PageContainer from "../../layouts/PageContainer";

import ProfileHeader from "../../components/student/profile/ProfileHeader";
import PersonalInfo from "../../components/student/profile/PersonalInfo";
import AcademicInfo from "../../components/student/profile/AcademicInfo";
import ContactInfo from "../../components/student/profile/ContactInfo";
import ParentInfo from "../../components/student/profile/ParentInfo";
import ResumeCard from "../../components/student/profile/ResumeCard";
import SkillsCard from "../../components/student/profile/SkillsCard";
import CertificatesCard from "../../components/student/profile/CertificatesCard";
import SocialLinks from "../../components/student/profile/SocialLinks";

import EditProfileModal from "../../components/student/profile/modals/EditProfileModal";

export default function StudentProfile() {
  const [showEditModal, setShowEditModal] = useState(false);
  const [student, setStudent] = useState({
    // Personal
    fullName: "Angel Manohar",
    gender: "Female",
    dob: "29 September 2005",
    bloodGroup: "O+",
    nationality: "Indian",
    aadhaar: "XXXX XXXX 4589",

    // Contact
    email: "angel.manohar@vsit.edu.in",
    phone: "+91 9876543210",
    emergencyContact: "+91 9876543211",
    address: "Vidyavihar, Mumbai",
    city: "Mumbai",
    state: "Maharashtra",

    // Academic
    rollNo: "24315A0036",
    department: "Data Science",
    program: "B.Sc Data Science",
    division: "A",
    semester: 5,
    cgpa: 8.62,
    academicYear: "2026–27",
    admissionYear: 2024,
    graduationYear: 2027,
    credits: 96,

    // Parents
    fatherName: "Stalin Manohar",
    fatherOccupation: "Business",
    motherName: "Jeya Stalin",
    motherOccupation: "Homemaker",
    parentPhone: "+91 9876543222",
    parentEmail: "parents@example.com",

    // Resume
    resumeUpdated: "10 July 2026",

    // Social
    linkedin: "linkedin.com/in/angelmanohar",
    github: "github.com/angelmanohar",
    portfolio: "angelmanohar.dev",
    leetcode: "leetcode.com/u/angelmanohar",
    hackerrank: "hackerrank.com/angelmanohar",
  });

  return (
    <PageContainer>

      <ProfileHeader 
      student={student} 
      onEditProfile={() => setShowEditModal(true)}
      />

      <div className="mt-10 grid grid-cols-1 gap-8 xl:grid-cols-2">
        <PersonalInfo student={student} />
        <AcademicInfo student={student} />
      </div>

      <div className="mt-10 grid grid-cols-1 gap-8 xl:grid-cols-2">
        <ContactInfo student={student} />
        <ParentInfo student={student} />
      </div>

      <div className="mt-10 grid grid-cols-1 gap-8 xl:grid-cols-2">
        <ResumeCard student={student} />
        <SkillsCard student={student} />
      </div>

      <div className="mt-10">
        <CertificatesCard />
      </div>

      <div className="mt-10">
        <SocialLinks student={student} />
      </div>

      {showEditModal && (
        <EditProfileModal
        student={student}
        onSave={setStudent}
        onClose={() => setShowEditModal(false)}
        />
      )}

    </PageContainer>
  );
}