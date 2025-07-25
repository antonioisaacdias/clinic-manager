import { PropsWithChildren } from "react";
import AppProvider from "@/components/app-provider";
import "@/styles/globals.css";

export default function RootLayout({ children }: PropsWithChildren) {
  return (
    <html lang="pt-BR">
      <body className="flex flex-col h-screen bg-gray-100">
        <AppProvider>
          {children}
        </AppProvider>
      </body>
    </html>
  );
}


