import AppSidebar from "@/components/app-sidebar";
import AppHeader from "@/components/app-header";
import { PropsWithChildren } from "react";
import { SidebarInset } from "@/components/ui/sidebar";
import ProtectedRoute from "@/components/protected-route";

export default function ApplicationLayout({ children }: PropsWithChildren) {
  return (
    <ProtectedRoute>
      <AppSidebar />
      <SidebarInset>
        <AppHeader hideOnPages={['/', '/welcome']} />
        <main className="flex flex-1 flex-col gap-4 p-4">
          {children}
        </main>
      </SidebarInset>
    </ProtectedRoute>
  );
}