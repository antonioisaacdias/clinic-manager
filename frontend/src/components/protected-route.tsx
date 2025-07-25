"use client";

import { useAuth } from "@/hooks/use-auth";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Loader2 } from "lucide-react";

interface ProtectedRouteProps {
  children: React.ReactNode;
  redirectTo?: string;
}

export default function ProtectedRoute({ 
  children, 
  redirectTo = "/login" 
}: ProtectedRouteProps) {
  const { isAuthenticated, isLoading } = useAuth();
  const router = useRouter();
  const [mounted, setMounted] = useState(false);

  // Evitar problemas de hidratação
  useEffect(() => {
    setMounted(true);
  }, []);

  // Redirecionar se não estiver autenticado
  useEffect(() => {
    if (mounted && !isLoading && !isAuthenticated) {
      console.log('🔓 Usuário não autenticado, redirecionando para:', redirectTo);
      router.push(redirectTo);
    }
  }, [isAuthenticated, isLoading, router, redirectTo, mounted]);

  // Loading centralizado enquanto não monta
  if (!mounted) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-white">
        <div className="flex flex-col items-center gap-4">
          <Loader2 className="h-8 w-8 animate-spin text-dark-teal" />
          <span className="text-sm text-gray-600">Carregando aplicação...</span>
        </div>
      </div>
    );
  }

  // Loading centralizado enquanto verifica autenticação
  if (isLoading) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-white">
        <div className="flex flex-col items-center gap-4">
          <Loader2 className="h-8 w-8 animate-spin text-dark-teal" />
          <span className="text-sm text-gray-600">Verificando autenticação...</span>
        </div>
      </div>
    );
  }

  // Se não estiver autenticado, mostrar loading de redirecionamento
  if (!isAuthenticated) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-white">
        <div className="flex flex-col items-center gap-4">
          <Loader2 className="h-8 w-8 animate-spin text-red-500" />
          <span className="text-sm text-gray-600">Redirecionando para login...</span>
        </div>
      </div>
    );
  }

  // Se estiver autenticado, renderizar o conteúdo
  return <>{children}</>;
}