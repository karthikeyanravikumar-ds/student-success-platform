import { Outlet } from "react-router-dom";

import Sidebar from "../components/common/Sidebar";
import Navbar from "../components/common/Navbar";
import MainContent from "./MainContent";

export default function DashboardLayout() {
  return (
    <div className="flex h-screen">
      <Sidebar />

      <MainContent>
        <Navbar />
        
        <div className="px-8 py-6">
          <Outlet />
        </div>

      </MainContent>
    </div>
  );
}