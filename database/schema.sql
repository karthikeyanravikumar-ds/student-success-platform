CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "roles" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "role_name" varchar(50) UNIQUE NOT NULL,
  "description" text,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "users" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "role_id" uuid NOT NULL,
  "email" varchar(255) UNIQUE NOT NULL,
  "password_hash" text NOT NULL,
  "is_active" boolean DEFAULT true,
  "last_login" timestamp,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "departments" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "department_code" varchar(10) UNIQUE NOT NULL,
  "department_name" varchar(100) NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "programs" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "department_id" uuid NOT NULL,
  "program_name" varchar(100) NOT NULL,
  "degree" varchar(50),
  "duration_years" int,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "students" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "user_id" uuid UNIQUE NOT NULL,
  "program_id" uuid NOT NULL,
  "department_id" uuid NOT NULL,
  "roll_no" varchar(20) UNIQUE NOT NULL,
  "full_name" varchar(150) NOT NULL,
  "gender" varchar(20),
  "dob" date,
  "phone" varchar(15),
  "division" varchar(10),
  "admission_year" int,
  "graduation_year" int,
  "current_semester" int,
  "profile_photo_path" text,
  "is_active" boolean DEFAULT true,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "faculty" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "user_id" uuid UNIQUE NOT NULL,
  "department_id" uuid NOT NULL,
  "faculty_code" varchar(20) UNIQUE NOT NULL,
  "full_name" varchar(150) NOT NULL,
  "designation" varchar(100),
  "qualification" varchar(150),
  "department_coordinator" boolean DEFAULT false,
  "coordinator_department_id" uuid,
  "phone" varchar(15),
  "joining_date" date,
  "profile_photo_path" text,
  "is_active" boolean DEFAULT true,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "academic_years" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "academic_year" varchar(20) UNIQUE NOT NULL,
  "start_date" date,
  "end_date" date,
  "is_current" boolean DEFAULT false,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "semesters" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "academic_year_id" uuid NOT NULL,
  "semester_number" int NOT NULL
  CHECK (semester_number BETWEEN 1 AND 6),
  "start_date" date,
  "end_date" date,
  "is_current" boolean DEFAULT false,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "subjects" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "department_id" uuid NOT NULL,
  "faculty_id" uuid NOT NULL,
  "semester_id" uuid NOT NULL,
  "subject_code" varchar(20) UNIQUE NOT NULL,
  "subject_name" varchar(150) NOT NULL,
  "credits" int,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "semester_results" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "student_id" uuid NOT NULL,
  "semester_id" uuid NOT NULL,
  "sgpa" decimal(3,2),
  "cgpa" decimal(3,2)
  CHECK (cgpa BETWEEN 0 AND 10),
  "result" varchar(20),
  "published_at" timestamp,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "student_marks" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "student_id" uuid NOT NULL,
  "subject_id" uuid NOT NULL,
  "internal_marks" decimal(5,2)
  CHECK (internal_marks >= 0),
  "external_marks" decimal(5,2)
  CHECK (external_marks >= 0),
  "total_marks" decimal(5,2),
  "grade" varchar(5),
  "result" varchar(20),
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "attendance" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "student_id" uuid NOT NULL,
  "subject_id" uuid NOT NULL,
  "attendance_percentage" decimal(5,2)
  CHECK (attendance_percentage BETWEEN 0 AND 100),
  "last_synced" timestamp,
  "source" varchar(50),
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "certificate_categories" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "category_name" varchar(100) UNIQUE NOT NULL,
  "description" text,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "certificates" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "student_id" uuid NOT NULL,
  "category_id" uuid NOT NULL,
  "verified_by" uuid,
  "title" varchar(255) NOT NULL,
  "issuing_organization" varchar(255),
  "issue_date" date,
  "expiry_date" date,
  "credential_id" varchar(100),
  "credential_url" text,
  "certificate_file" text,
  "verification_status" varchar(20) DEFAULT 'Pending',
  "verification_remarks" text,
  "verified_at" timestamp,
  "uploaded_at" timestamp,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "certificate_verification_logs" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "certificate_id" uuid NOT NULL,
  "verified_by" uuid NOT NULL,
  "previous_status" varchar(20),
  "new_status" varchar(20),
  "remarks" text,
  "action_date" timestamp
);

CREATE TABLE "companies" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "company_name" varchar(255) UNIQUE NOT NULL,
  "company_logo" text,
  "website" text,
  "industry" varchar(100),
  "company_description" text,
  "hr_name" varchar(150),
  "hr_email" varchar(255),
  "hr_phone" varchar(20),
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "placement_drives" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "company_id" uuid NOT NULL,
  "drive_title" varchar(255) NOT NULL,
  "drive_type" varchar(50),
  "campus_mode" varchar(50),
  "location" varchar(255),
  "package" decimal(10,2),
  "bond_details" text,
  "registration_deadline" date,
  "drive_date" date,
  "job_description" text,
  "status" varchar(30),
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "job_roles" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "placement_drive_id" uuid NOT NULL,
  "role_name" varchar(150) NOT NULL,
  "openings" int,
  "package" decimal(10,2),
  "description" text,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "drive_eligibility" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "placement_drive_id" uuid NOT NULL,
  "minimum_cgpa" decimal(3,2),
  "max_active_backlogs" int,
  "max_total_backlogs" int,
  "graduation_year" int,
  "department_id" uuid,
  "program_id" uuid,
  "additional_criteria" text,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "placement_statuses" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "status_name" varchar(50) UNIQUE NOT NULL,
  "description" text
);

CREATE TABLE "student_applications" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "student_id" uuid NOT NULL,
  "placement_drive_id" uuid NOT NULL,
  "status_id" uuid NOT NULL,
  "resume_url" text,
  "applied_at" timestamp,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "application_status_history" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "application_id" uuid NOT NULL,
  "status_id" uuid NOT NULL,
  "updated_by" uuid NOT NULL,
  "remarks" text,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "interview_rounds" (
  "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "placement_drive_id" uuid NOT NULL,
  "round_number" int,
  "round_name" varchar(100),
  "round_type" varchar(100),
  "scheduled_date" timestamp,
  "result_status" varchar(30),
  "remarks" text,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- FOREIGN KEY CONSTRAINTS
-- =====================================================

-- Users
ALTER TABLE users
ADD CONSTRAINT fk_users_role
FOREIGN KEY (role_id)
REFERENCES roles(id)
ON DELETE RESTRICT;

-- Programs
ALTER TABLE programs
ADD CONSTRAINT fk_programs_department
FOREIGN KEY (department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

-- Students
ALTER TABLE students
ADD CONSTRAINT fk_students_user
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE;

ALTER TABLE students
ADD CONSTRAINT fk_students_department
FOREIGN KEY (department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

ALTER TABLE students
ADD CONSTRAINT fk_students_program
FOREIGN KEY (program_id)
REFERENCES programs(id)
ON DELETE RESTRICT;

-- Faculty
ALTER TABLE faculty
ADD CONSTRAINT fk_faculty_user
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE;

ALTER TABLE faculty
ADD CONSTRAINT fk_faculty_department
FOREIGN KEY (department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

ALTER TABLE faculty
ADD CONSTRAINT fk_faculty_coordinator_department
FOREIGN KEY (coordinator_department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

-- Semesters
ALTER TABLE semesters
ADD CONSTRAINT fk_semesters_academic_year
FOREIGN KEY (academic_year_id)
REFERENCES academic_years(id)
ON DELETE RESTRICT;

-- Subjects
ALTER TABLE subjects
ADD CONSTRAINT fk_subjects_department
FOREIGN KEY (department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

ALTER TABLE subjects
ADD CONSTRAINT fk_subjects_faculty
FOREIGN KEY (faculty_id)
REFERENCES faculty(id)
ON DELETE RESTRICT;

ALTER TABLE subjects
ADD CONSTRAINT fk_subjects_semester
FOREIGN KEY (semester_id)
REFERENCES semesters(id)
ON DELETE RESTRICT;

-- Semester Results
ALTER TABLE semester_results
ADD CONSTRAINT fk_semester_results_student
FOREIGN KEY (student_id)
REFERENCES students(id)
ON DELETE CASCADE;

ALTER TABLE semester_results
ADD CONSTRAINT fk_semester_results_semester
FOREIGN KEY (semester_id)
REFERENCES semesters(id)
ON DELETE RESTRICT;

-- Student Marks
ALTER TABLE student_marks
ADD CONSTRAINT fk_student_marks_student
FOREIGN KEY (student_id)
REFERENCES students(id)
ON DELETE CASCADE;

ALTER TABLE student_marks
ADD CONSTRAINT fk_student_marks_subject
FOREIGN KEY (subject_id)
REFERENCES subjects(id)
ON DELETE RESTRICT;

-- Attendance
ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_student
FOREIGN KEY (student_id)
REFERENCES students(id)
ON DELETE CASCADE;

ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_subject
FOREIGN KEY (subject_id)
REFERENCES subjects(id)
ON DELETE RESTRICT;

-- Certificates
ALTER TABLE certificates
ADD CONSTRAINT fk_certificates_student
FOREIGN KEY (student_id)
REFERENCES students(id)
ON DELETE CASCADE;

ALTER TABLE certificates
ADD CONSTRAINT fk_certificates_category
FOREIGN KEY (category_id)
REFERENCES certificate_categories(id)
ON DELETE RESTRICT;

ALTER TABLE certificates
ADD CONSTRAINT fk_certificates_verified_by
FOREIGN KEY (verified_by)
REFERENCES faculty(id)
ON DELETE SET NULL;

-- Certificate Verification Logs
ALTER TABLE certificate_verification_logs
ADD CONSTRAINT fk_certificate_logs_certificate
FOREIGN KEY (certificate_id)
REFERENCES certificates(id)
ON DELETE CASCADE;

ALTER TABLE certificate_verification_logs
ADD CONSTRAINT fk_certificate_logs_verified_by
FOREIGN KEY (verified_by)
REFERENCES faculty(id)
ON DELETE RESTRICT;

-- Companies & Placement
ALTER TABLE placement_drives
ADD CONSTRAINT fk_placement_drives_company
FOREIGN KEY (company_id)
REFERENCES companies(id)
ON DELETE CASCADE;

ALTER TABLE job_roles
ADD CONSTRAINT fk_job_roles_drive
FOREIGN KEY (placement_drive_id)
REFERENCES placement_drives(id)
ON DELETE CASCADE;

ALTER TABLE drive_eligibility
ADD CONSTRAINT fk_drive_eligibility_drive
FOREIGN KEY (placement_drive_id)
REFERENCES placement_drives(id)
ON DELETE CASCADE;

ALTER TABLE drive_eligibility
ADD CONSTRAINT fk_drive_eligibility_department
FOREIGN KEY (department_id)
REFERENCES departments(id)
ON DELETE RESTRICT;

ALTER TABLE drive_eligibility
ADD CONSTRAINT fk_drive_eligibility_program
FOREIGN KEY (program_id)
REFERENCES programs(id)
ON DELETE RESTRICT;

-- Student Applications
ALTER TABLE student_applications
ADD CONSTRAINT fk_student_applications_student
FOREIGN KEY (student_id)
REFERENCES students(id)
ON DELETE CASCADE;

ALTER TABLE student_applications
ADD CONSTRAINT fk_student_applications_drive
FOREIGN KEY (placement_drive_id)
REFERENCES placement_drives(id)
ON DELETE CASCADE;

ALTER TABLE student_applications
ADD CONSTRAINT fk_student_applications_status
FOREIGN KEY (status_id)
REFERENCES placement_statuses(id)
ON DELETE RESTRICT;

-- Application Status History
ALTER TABLE application_status_history
ADD CONSTRAINT fk_application_history_application
FOREIGN KEY (application_id)
REFERENCES student_applications(id)
ON DELETE CASCADE;

ALTER TABLE application_status_history
ADD CONSTRAINT fk_application_history_status
FOREIGN KEY (status_id)
REFERENCES placement_statuses(id)
ON DELETE RESTRICT;

ALTER TABLE application_status_history
ADD CONSTRAINT fk_application_history_updated_by
FOREIGN KEY (updated_by)
REFERENCES faculty(id)
ON DELETE RESTRICT;

-- Interview Rounds
ALTER TABLE interview_rounds
ADD CONSTRAINT fk_interview_rounds_drive
FOREIGN KEY (placement_drive_id)
REFERENCES placement_drives(id)
ON DELETE CASCADE;

-- =====================================================
-- INDEXES
-- Student Success Platform (SSP)
-- =====================================================

-- =====================
-- USERS
-- =====================

CREATE INDEX idx_users_role
ON users(role_id);

CREATE INDEX idx_users_email
ON users(email);

-- =====================
-- STUDENTS
-- =====================

CREATE INDEX idx_students_roll_no
ON students(roll_no);

CREATE INDEX idx_students_department
ON students(department_id);

CREATE INDEX idx_students_program
ON students(program_id);

CREATE INDEX idx_students_graduation_year
ON students(graduation_year);

-- =====================
-- FACULTY
-- =====================

CREATE INDEX idx_faculty_department
ON faculty(department_id);

CREATE INDEX idx_faculty_code
ON faculty(faculty_code);

-- =====================
-- SUBJECTS
-- =====================

CREATE INDEX idx_subject_code
ON subjects(subject_code);

CREATE INDEX idx_subject_department
ON subjects(department_id);

CREATE INDEX idx_subject_faculty
ON subjects(faculty_id);

CREATE INDEX idx_subject_semester
ON subjects(semester_id);

-- =====================
-- SEMESTER RESULTS
-- =====================

CREATE INDEX idx_semester_results_student
ON semester_results(student_id);

CREATE INDEX idx_semester_results_semester
ON semester_results(semester_id);

-- =====================
-- STUDENT MARKS
-- =====================

CREATE INDEX idx_student_marks_student
ON student_marks(student_id);

CREATE INDEX idx_student_marks_subject
ON student_marks(subject_id);

-- =====================
-- ATTENDANCE
-- =====================

CREATE INDEX idx_attendance_student
ON attendance(student_id);

CREATE INDEX idx_attendance_subject
ON attendance(subject_id);

-- =====================
-- CERTIFICATES
-- =====================

CREATE INDEX idx_certificates_student
ON certificates(student_id);

CREATE INDEX idx_certificate_status
ON certificates(verification_status);

CREATE INDEX idx_certificate_category
ON certificates(category_id);

-- =====================
-- COMPANIES
-- =====================

CREATE INDEX idx_company_name
ON companies(company_name);

-- =====================
-- PLACEMENT DRIVES
-- =====================

CREATE INDEX idx_drive_company
ON placement_drives(company_id);

CREATE INDEX idx_drive_date
ON placement_drives(drive_date);

-- =====================
-- JOB ROLES
-- =====================

CREATE INDEX idx_job_roles_drive
ON job_roles(placement_drive_id);

-- =====================
-- STUDENT APPLICATIONS
-- =====================

CREATE INDEX idx_application_student
ON student_applications(student_id);

CREATE INDEX idx_application_drive
ON student_applications(placement_drive_id);

CREATE INDEX idx_application_status
ON student_applications(status_id);

-- =====================
-- APPLICATION HISTORY
-- =====================

CREATE INDEX idx_application_history_application
ON application_status_history(application_id);

-- =====================
-- INTERVIEW ROUNDS
-- =====================

CREATE INDEX idx_interview_drive
ON interview_rounds(placement_drive_id);