import AppSidebar from "@/components/app-sidebar";
import AppHeader from "@/components/app-header";
import { PropsWithChildren } from "react";
import { SidebarInset } from "@/components/ui/sidebar";

export default function ApplicationLayout({ children }: PropsWithChildren) {
  return (
    <>
      <AppSidebar />
      <SidebarInset>
        <AppHeader hideOnPages={['/', '/login']} />
        <main className="flex flex-1 flex-col gap-4 p-4">
          {children}
        </main>
      </SidebarInset>
    </>
  );
}