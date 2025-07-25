import api from "./api";
import Cookies from "js-cookie";

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface LoginResponse {
  access: string;
  refresh: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  first_name?: string;
  last_name?: string;
}

export const authService = {
  // 🔐 Login
  async login(credentials: LoginCredentials): Promise<LoginResponse> {
    try {
      const response = await api.post<LoginResponse>("auth/token/", credentials);
      
      // Salvar tokens em cookies seguros
      Cookies.set("access_token", response.data.access, {
        expires: 1 / 24, // 1 hora
        secure: process.env.NODE_ENV === "production",
        sameSite: "strict",
      });

      Cookies.set("refresh_token", response.data.refresh, {
        expires: 7, // 7 dias
        secure: process.env.NODE_ENV === "production",
        sameSite: "strict",
      });
      
      return response.data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || 
                          error.response?.data?.message || 
                          "Credenciais inválidas";
      throw new Error(errorMessage);
    }
  },

  // 👤 Obter perfil do usuário
  async getProfile(): Promise<User> {
    try {
      const response = await api.get<User>("users/profile/");
      return response.data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || 
                          "Erro ao carregar perfil";
      throw new Error(errorMessage);
    }
  },

  // ✏️ Atualizar perfil
  async updateProfile(data: Partial<User>): Promise<User> {
    try {
      const response = await api.patch<User>("users/profile/", data);
      return response.data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || 
                          "Erro ao atualizar perfil";
      throw new Error(errorMessage);
    }
  },

  // 🔓 Logout
  async logout(): Promise<void> {
    try {
      const refreshToken = Cookies.get("refresh_token");
      
      // Tentar fazer blacklist do token no backend
      if (refreshToken) {
        await api.post("auth/token/blacklist/", {
          refresh: refreshToken,
        });
      }
    } catch (error) {
      console.error("Erro ao fazer blacklist do token:", error);
    } finally {
      // Sempre limpar cookies localmente
      Cookies.remove("access_token");
      Cookies.remove("refresh_token");
    }
  },

  async forgotPassword(email: string): Promise<{ message: string }> {
    try {
      const response = await api.post("auth/password-reset/", { email });
      return response.data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || 
                          "Erro ao enviar email de recuperação";
      throw new Error(errorMessage);
    }
  },

  async changePassword(oldPassword: string, newPassword: string): Promise<{ message: string }> {
    try {
      const response = await api.post("auth/password-change/", {
        old_password: oldPassword,
        new_password: newPassword,
      });
      return response.data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || 
                          "Erro ao alterar senha";
      throw new Error(errorMessage);
    }
  },

  isAuthenticated(): boolean {
    return !!Cookies.get("access_token");
  },

  getAccessToken(): string | null {
    return Cookies.get("access_token") || null;
  },

  getRefreshToken(): string | null {
    return Cookies.get("refresh_token") || null;
  },
};
