import Image from "next/image";

export default function AuthBanner() {
  return (
    <aside className="bg-dark-teal p-4 flex flex-col justify-between items-center text-center text-white flex-1">
      {/* Conteúdo principal centralizado */}
      <div className="flex-1 flex flex-col justify-center items-center pb-8">
        <div className="flex items-center mb-4 flex-col gap-3">
            <Image
              src="/assets/imgs/logo.png"
              alt="Descrição da imagem"
              width={100}
              height={100}
              className="rounded-lg"
            />
            <h1 className="text-4xl font-bold">Instituto Sarang</h1>
        </div>
        <h2 className="text-2xl font-bold text-gray-200">Bem-vindo de volta</h2>
        <p className="mt-2 text-gray-200">Por favor, insira suas credenciais para continuar.</p>
      </div>
      
      {/* Footer fixo no pé */}
      <p className="text-xs text-gray-300 mt-4">
        Feito com ♥ por <span className="font-semibold">Antonio Dias</span>
      </p>
    </aside>
  );
}