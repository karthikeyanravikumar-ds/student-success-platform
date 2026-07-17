import PageContainer from "../../layouts/PageContainer";

import ProfileSettings from "../../components/student/settings/ProfileSettings";
import NotificationSettings from "../../components/student/settings/NotificationSettings";
import AppearanceSettings from "../../components/student/settings/AppearanceSettings";
import SecuritySettings from "../../components/student/settings/SecuritySettings";
import PrivacySettings from "../../components/student/settings/PrivacySettings";
import SettingsActions from "../../components/student/settings/SettingsActions";


export default function Settings() {
  return (
    <PageContainer>

  <div className="mb-8">
    <h1 className="text-4xl font-bold">
      Settings
    </h1>

    <p className="text-gray-500">
      Manage your account, security and application preferences.
    </p>
  </div>


  <div className="mt-8">
    <ProfileSettings />
  </div>

  <div className="mt-8">
    <NotificationSettings />
  </div>

  <div className="mt-8">
    <AppearanceSettings />
  </div>

  <div className="mt-8">
    <SecuritySettings />
  </div>

  <div className="mt-8">
    <PrivacySettings />
  </div>

  <div className="mt-8">
    <SettingsActions />
  </div>

</PageContainer>
  );
}