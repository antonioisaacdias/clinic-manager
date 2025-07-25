import Image from 'next/image';
import { AlertTriangle } from 'lucide-react';

export default function NotFound() {
  return (
    <div className="flex-1 bg-gradient-to-br from-gray-50 to-gray-100 flex items-center justify-center px-4">
      <div className="max-w-2xl w-full">
        {/* Container principal */}
        <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
          
          {/* Header com cor do tema */}
          <div className="bg-dark-teal px-8 py-6">
            <div className="flex items-center justify-center gap-4">
              <Image
                src="/assets/imgs/logo.png"
                alt="Instituto Sarang"
                width={60}
                height={60}
                className="rounded-lg"
              />
              <div className="text-center">
                <h1 className="text-white text-xl font-bold">
                  Instituto Sarang
                </h1>
                <p className="text-gray-200 text-sm">
                  Clinic Manager
                </p>
              </div>
            </div>
          </div>

          {/* Conteúdo principal */}
          <div className="px-8 py-12 text-center">
            
            {/* Ícone e número 404 */}
            <div className="mb-8">
              <div className="mx-auto w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mb-6">
                <AlertTriangle className="w-10 h-10 text-red-500" />
              </div>
              
              <h2 className="text-8xl font-bold text-dark-teal mb-4 tracking-tight">
                404
              </h2>
              
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">
                Página não encontrada
              </h3>
              
              <p className="text-gray-600 text-lg max-w-md mx-auto leading-relaxed">
                Ops! A página que você está procurando não existe ou foi movida para outro local.
              </p>
            </div>
          </div>

          {/* Footer */}
          <div className="bg-gray-50 px-8 py-4 border-t border-gray-200">
            <p className="text-center text-xs text-gray-500">
              Made with ♥ by <span className="font-semibold text-dark-teal">Antonio Dias</span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

// Metadata para SEO
export const metadata = {
  title: '404 - Página não encontrada | Instituto Sarang',
  description: 'A página que você procura não foi encontrada no sistema Clinic Manager.',
};