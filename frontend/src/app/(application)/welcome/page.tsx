import Image from "next/image"
import Link from "next/link"
import { ArrowRight, Users, Calendar, Activity } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function Page() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[calc(100vh-200px)] text-center space-y-8">
      {/* Logo */}
      <div className="mb-8">
        <Image
          src="/assets/imgs/logo.png"
          alt="Clinic Manager"
          width={120}
          height={120}
          className="mx-auto"
          priority
        />
      </div>

      {/* Título e Descrição */}
      <div className="space-y-4">
        <h1 className="text-4xl font-bold text-gray-900">
          Bem-vindo ao Clinic Manager
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl">
          Sua plataforma completa para gerenciamento de clínicas médicas.
          Simplifique seus processos e melhore o atendimento aos pacientes.
        </p>
      </div>

      {/* Cards de Funcionalidades */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12 w-full max-w-4xl">
        <div className="bg-white p-6 rounded-lg shadow-sm border hover:shadow-md transition-shadow">
          <Users className="w-8 h-8 text-blue-600 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Gestão de Pacientes
          </h3>
          <p className="text-gray-600 text-sm">
            Cadastre e gerencie informações dos seus pacientes de forma organizada
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-sm border hover:shadow-md transition-shadow">
          <Calendar className="w-8 h-8 text-green-600 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Agendamentos
          </h3>
          <p className="text-gray-600 text-sm">
            Controle consultas e procedimentos com agenda inteligente
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-sm border hover:shadow-md transition-shadow">
          <Activity className="w-8 h-8 text-purple-600 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            Relatórios
          </h3>
          <p className="text-gray-600 text-sm">
            Acompanhe métricas e gere relatórios detalhados da sua clínica
          </p>
        </div>
      </div>

      {/* Mensagem de Rodapé */}
      <div className="mt-12 p-4 bg-blue-50 rounded-lg border border-blue-200 max-w-2xl">
        <p className="text-blue-800 text-sm">
          💡 Use o menu lateral para navegar entre as funcionalidades do sistema
        </p>
      </div>
    </div>
  );
}