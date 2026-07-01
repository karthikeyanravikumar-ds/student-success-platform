-- =====================================================
-- Student Success Platform (SSP)
-- seed.sql
-- Master Data Only
-- =====================================================

BEGIN;

-- =====================
-- ROLES
-- =====================
INSERT INTO roles (id, role_name, description)
VALUES
(uuid_generate_v4(),'Student','Student Portal User'),
(uuid_generate_v4(),'Faculty','Faculty Member'),
(uuid_generate_v4(),'Placement Officer','Placement Cell Staff'),
(uuid_generate_v4(),'Administrator','System Administrator')
ON CONFLICT (role_name) DO NOTHING;

-- =====================
-- DEPARTMENTS
-- =====================
INSERT INTO departments (id, department_code, department_name)
VALUES
(uuid_generate_v4(),'315','Data Science'),
(uuid_generate_v4(),'205','Information Technology'),
(uuid_generate_v4(),'206','Computer Science (Artificial Intelligence & Machine Learning)'),
(uuid_generate_v4(),'204','Computer Science (Software Engineering)'),
(uuid_generate_v4(),'203','Data Science & Artificial Intelligence')

ON CONFLICT (department_code)
DO UPDATE SET
department_name = EXCLUDED.department_name;

-- =====================
-- PROGRAMS
-- =====================
INSERT INTO programs
(id, department_id, program_name, degree, duration_years)

SELECT
uuid_generate_v4(),
id,
'Data Science',
'B.Sc',
3
FROM departments
WHERE department_code='315';

INSERT INTO programs
(id, department_id, program_name, degree, duration_years)

SELECT
uuid_generate_v4(),
id,
'Information Technology',
'B.Sc',
3
FROM departments
WHERE department_code='205';

INSERT INTO programs
(id, department_id, program_name, degree, duration_years)

SELECT
uuid_generate_v4(),
id,
'Computer Science (Artificial Intelligence & Machine Learning)',
'B.Sc',
3
FROM departments
WHERE department_code='206';

INSERT INTO programs
(id, department_id, program_name, degree, duration_years)

SELECT
uuid_generate_v4(),
id,
'Computer Science (Software Engineering)',
'B.Sc',
3
FROM departments
WHERE department_code='204';

INSERT INTO programs
(id, department_id, program_name, degree, duration_years)

SELECT
uuid_generate_v4(),
id,
'Data Science & Artificial Intelligence',
'M.Sc',
2

FROM departments
WHERE department_code='203';

-- =====================
-- ACADEMIC YEAR
-- =====================
INSERT INTO academic_years
(id,academic_year,start_date,end_date,is_current)
VALUES
(uuid_generate_v4(),'2026-2027','2026-07-01','2027-06-30',TRUE)
ON CONFLICT (academic_year) DO NOTHING;

-- =====================
-- SEMESTERS
-- =====================
INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,1,'2026-07-01','2026-11-30',FALSE
FROM academic_years WHERE academic_year='2026-2027';

INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,2,'2026-12-01','2027-04-30',FALSE
FROM academic_years WHERE academic_year='2026-2027';

INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,3,'2027-07-01','2027-11-30',FALSE
FROM academic_years WHERE academic_year='2026-2027';

INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,4,'2027-12-01','2028-04-30',FALSE
FROM academic_years WHERE academic_year='2026-2027';

INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,5,'2028-07-01','2028-11-30',TRUE
FROM academic_years WHERE academic_year='2026-2027';

INSERT INTO semesters(id,academic_year_id,semester_number,start_date,end_date,is_current)
SELECT uuid_generate_v4(),id,6,'2028-12-01','2029-04-30',FALSE
FROM academic_years WHERE academic_year='2026-2027';

-- =====================
-- CERTIFICATE CATEGORIES
-- =====================
INSERT INTO certificate_categories(id,category_name,description)
VALUES
(uuid_generate_v4(),'AWS','Amazon Web Services'),
(uuid_generate_v4(),'Google','Google Certifications'),
(uuid_generate_v4(),'Microsoft','Microsoft Certifications'),
(uuid_generate_v4(),'NPTEL','NPTEL Courses'),
(uuid_generate_v4(),'Coursera','Coursera Courses'),
(uuid_generate_v4(),'Internship','Internship Completion'),
(uuid_generate_v4(),'Hackathon','Hackathon Participation'),
(uuid_generate_v4(),'Workshop','Workshop Participation'),
(uuid_generate_v4(),'Research Paper','Research Publications'),
(uuid_generate_v4(),'Sports','Sports Achievement'),
(uuid_generate_v4(),'Cultural','Cultural Activities'),
(uuid_generate_v4(),'Other','Other Certificates')
ON CONFLICT (category_name) DO NOTHING;

-- =====================
-- PLACEMENT STATUSES
-- =====================
INSERT INTO placement_statuses(id,status_name,description)
VALUES
(uuid_generate_v4(),'Applied','Application Submitted'),
(uuid_generate_v4(),'Shortlisted','Shortlisted'),
(uuid_generate_v4(),'Assessment','Assessment Round'),
(uuid_generate_v4(),'Technical Interview','Technical Interview'),
(uuid_generate_v4(),'HR Interview','HR Interview'),
(uuid_generate_v4(),'Selected','Selected'),
(uuid_generate_v4(),'Rejected','Rejected'),
(uuid_generate_v4(),'Offer Accepted','Offer Accepted'),
(uuid_generate_v4(),'Offer Declined','Offer Declined')
ON CONFLICT (status_name) DO NOTHING;

-- =====================
-- DEFAULT ADMIN USER
-- Replace password hash after implementing authentication.
-- =====================
INSERT INTO users(id,role_id,email,password_hash,is_active)
SELECT
uuid_generate_v4(),
r.id,
'admin@vsit.edu.in',
'REPLACE_WITH_BCRYPT_HASH',
TRUE
FROM roles r
WHERE r.role_name='Administrator'
AND NOT EXISTS (
SELECT 1 FROM users WHERE email='admin@vsit.edu.in'
);

COMMIT;
