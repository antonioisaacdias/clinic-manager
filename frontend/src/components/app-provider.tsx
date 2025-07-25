"use client"

import { PropsWithChildren } from "react"
import { SidebarProvider } from "./ui/sidebar"
import QueryProvider from "./query-provider"

export default function AppProvider({ children }: PropsWithChildren) {
  return (
    <QueryProvider>
      <SidebarProvider>
        {children}
      </SidebarProvider>
    </QueryProvider>
  )
}
