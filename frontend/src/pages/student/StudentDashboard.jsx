import { useEffect, useState } from "react";

import { getMyProfile } from "../../services/studentService";
import { getStudentDashboard } from "../../services/dashboardService";

import DashboardHeader from "../../components/student/dashboard/DashboardHeader";
import DashboardStats from "../../components/student/dashboard/DashboardStats";
import AttendanceChart from "../../components/student/dashboard/AttendanceChart";
import CgpaChart from "../../components/student/dashboard/CgpaChart";
import UpcomingExams from "../../components/student/dashboard/UpcomingExams";
import RecentResults from "../../components/student/dashboard/RecentResults";
import QuickActions from "../../components/student/dashboard/QuickActions";
import PageContainer from "../../layouts/PageContainer";

export default function StudentDashboard() {

    const [student, setStudent] = useState(null);
    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {
    async function loadData() {
        try {
            const [profile, dashboardData] = await Promise.all([
                getMyProfile(),
                getStudentDashboard(),
            ]);

            console.log("Profile:", profile);
            console.log("Dashboard:", dashboardData);

            setStudent(profile);
            setDashboard(dashboardData);
        } catch (err) {
            console.error("Dashboard Error:", err);
        }
    }

    loadData();
}, []);

    if (!student || !dashboard) {
        return <div>Loading...</div>;
    }

    return (

        <PageContainer>

            <DashboardHeader student={student} />

            <DashboardStats dashboard={dashboard} />

            <div className="mt-8 grid grid-cols-1 gap-6 xl:grid-cols-2">

                <AttendanceChart dashboard={dashboard} />

                <CgpaChart dashboard={dashboard} />

            </div>

            <div className="mt-8 grid grid-cols-1 gap-6 xl:grid-cols-2">

                <UpcomingExams dashboard={dashboard} />

                <RecentResults dashboard={dashboard} />

            </div>

            <div className="mt-8">

                <QuickActions dashboard={dashboard} />

            </div>

        </PageContainer>

    );

}