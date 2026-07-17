import PageContainer from "../../layouts/PageContainer";

import NotificationToolbar from "../../components/student/notifications/NotificationToolbar";
import PinnedAlerts from "../../components/student/notifications/PinnedAlerts";
import NotificationList from "../../components/student/notifications/NotificationList";

export default function Notifications() {
  return (
    <PageContainer>

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Notifications
        </h1>

        <p className="text-gray-500">
          Stay updated with all academic and placement activities.
        </p>

      </div>

      <NotificationToolbar />

      <PinnedAlerts />


      <div className="mt-6">
        <NotificationList />
      </div>

    </PageContainer>
  );
}