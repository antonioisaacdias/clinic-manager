import { authService, LoginCredentials } from '@/services/auth';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

export const useAuth = () => {
  const queryClient = useQueryClient();
  const router = useRouter();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  // 👤 Query para perfil do usuário
  const {
    data: user,
    isLoading: isLoadingUser,
    error: userError,
    refetch: refetchUser,
  } = useQuery({
    queryKey: ['user', 'profile'],
    queryFn: authService.getProfile,
    enabled: mounted && authService.isAuthenticated(), // ✅ Só executa após montar
    retry: false,
    staleTime: 1000 * 60 * 5, // 5 minutos
  });

  // 🔐 Mutation para login
  const loginMutation = useMutation({
    mutationFn: authService.login,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['user'] });
      router.push('/welcome');
    },
    onError: (error: Error) => {
      console.error('Erro no login:', error.message);
    },
  });

  // 🔓 Mutation para logout
  const logoutMutation = useMutation({
    mutationFn: authService.logout,
    onSuccess: () => {
      queryClient.clear();
      router.push('/login');
    },
    onError: (error: Error) => {
      console.error('Erro no logout:', error.message);
      router.push('/login');
    },
  });

  return {
    // 📊 Estados
    user,
    isAuthenticated: mounted ? authService.isAuthenticated() : false, // ✅ Evitar hidratação
    isLoading: !mounted || isLoadingUser || 
               loginMutation.isPending || 
               logoutMutation.isPending,
    
    // 🔧 Funções principais
    login: (credentials: LoginCredentials) => loginMutation.mutate(credentials),
    logout: () => logoutMutation.mutate(),
    
    // 🎯 Estados específicos das mutations
    loginState: {
      isLoading: loginMutation.isPending,
      error: loginMutation.error,
      isSuccess: loginMutation.isSuccess,
    },
  };
};