"use client"

import { Sidebar } from "lucide-react"
import { PropsWithChildren } from "react"
import { SidebarProvider } from "./ui/sidebar"

export default function AppProvider({ children }: PropsWithChildren) {
  return (
    <SidebarProvider>
      {children}
    </SidebarProvider>
  )
}
