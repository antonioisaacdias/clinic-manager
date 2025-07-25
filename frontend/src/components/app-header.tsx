"use client"

import { SidebarTrigger } from "@/components/ui/sidebar";
import { usePathname } from "next/navigation";
import { ReactNode } from "react";

interface AppHeaderProps {
  title?: string;
  subtitle?: string;
  actions?: ReactNode;
  hideOnPages?: string[];
}

const PAGE_TITLES: Record<string, string> = {
  '/dashboard': 'Dashboard',
  '/patients': 'Pacientes',
  '/professionals': 'Profissionais', 
  '/administration': 'Administração',
  '/': 'Clinic Manager'
};

export default function AppHeader({ 
  title, 
  subtitle,
  actions,
  hideOnPages = ['/', '/welcome']
}: AppHeaderProps) {
  const pathname = usePathname();
  
  // Ocultar header em páginas específicas
  if (hideOnPages.includes(pathname)) {
    return null;
  }

  // Título automático baseado na rota ou personalizado
  const headerTitle = title || PAGE_TITLES[pathname] || 'Clinic Manager';

  return (
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 bg-white">
      
      <div className="flex-1 flex items-center justify-between">
        {/* Título e Subtítulo */}
        <div>
          <h2 className="text-lg font-semibold text-gray-900">
            {headerTitle}
          </h2>
          {subtitle && (
            <p className="text-sm text-gray-500">
              {subtitle}
            </p>
          )}
        </div>

        {/* Ações personalizadas */}
        {actions && (
          <div className="flex items-center gap-2">
            {actions}
          </div>
        )}
      </div>
    </header>
  );
}