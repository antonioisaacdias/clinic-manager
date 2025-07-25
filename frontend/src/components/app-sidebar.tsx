"use client"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { SquareChartGantt, ClipboardPlus, Stethoscope, LogOut } from "lucide-react"
import Link from "next/link"
import Image from "next/image"
import { usePathname } from "next/navigation"

const menuItems = [
  {
    title: "Profissionais",
    icon: Stethoscope,
    href: "/professionals",
  },
  {
    title: "Pacientes",
    icon: ClipboardPlus,
    href: "/patients",
  },
  {
    title: "Administração",
    icon: SquareChartGantt,
    href: "/administration",
  },
]

export default function AppSidebar() {
  const pathname = usePathname();

  return (
    <Sidebar 
      collapsible="icon"
      style={{
        '--sidebar-accent': '#267474',
        '--sidebar-accent-foreground': '#ffffff',
      } as React.CSSProperties}
    >
      <SidebarHeader className="bg-dark-teal">
        <div className="flex items-center justify-between p-4 group-data-[collapsible=icon]:justify-center">
          <Image
            src="/assets/imgs/logo.png"
            alt="Instituto Sarang"
            width={50}
            height={50}
            className="group-data-[collapsible=icon]:hidden"
          />
          <h1 className="text-xl font-bold text-white group-data-[collapsible=icon]:hidden ms-3 leading-tight text-gray-50">
            Instituto Sarang
          </h1>
          <SidebarTrigger className="ml-auto group-data-[collapsible=icon]:ml-0 text-gray-100 hover:text-gray-100 hover:bg-dark-teal-hover p-2 flex items-center justify-center rounded-md min-w-8 min-h-8" />
        </div>
      </SidebarHeader>
      
      <SidebarContent className="bg-dark-teal">
        <SidebarGroup>
          <SidebarGroupLabel className="text-gray-300">Menu Principal</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {menuItems.map((item) => {
                const isActive = pathname === item.href;
                
                return (
                  <SidebarMenuItem key={item.href}>
                    <SidebarMenuButton 
                      asChild 
                      tooltip={item.title}
                      className={`
                        text-gray-100 
                        hover:text-gray-100 
                        hover:bg-dark-teal-hover
                        ${isActive ? 'bg-dark-teal-hover text-gray-100' : ''}
                        data-[active=true]:bg-dark-teal-hover
                        data-[active=true]:text-gray-100
                      `}
                      isActive={isActive}
                    >
                      <Link href={item.href} className="text-gray-100">
                        <item.icon className="w-4 h-4" />
                        <span>{item.title}</span>
                      </Link>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                );
              })}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      
      <SidebarFooter className="bg-dark-teal">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton
              asChild
              tooltip="Sair"
              className={`
                text-gray-100 
                hover:text-gray-100 
                hover:bg-dark-teal-hover
                data-[active=true]:bg-dark-teal-hover
                data-[active=true]:text-gray-100
                h-12 px-4 my-2
                flex items-center justify-center
                text-base font-bold
              `}
              isActive={pathname === "/logout"}
            >
              <Link href="/logout" className="text-gray-100 flex items-center justify-center gap-3 w-full group-data-[collapsible=icon]:justify-center">
                <LogOut className="w-5 h-5" />
                <span className="text-base font-bold group-data-[collapsible=icon]:hidden">Sair</span>
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
        
        <div className="p-4 flex flex-col items-center">
          <p className="text-xs text-sidebar-foreground/60 group-data-[collapsible=icon]:hidden text-gray-300">
            Made with ♥ by <span className="font-semibold">Antonio Dias</span>
          </p>
        </div>
      </SidebarFooter>
    </Sidebar>
  )
}