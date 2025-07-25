
import { PropsWithChildren } from "react";

export default function AuthenticationLayout({ children }: PropsWithChildren) {
  return (
      <main className="flex flex-1 w-full items-center justify-center">
        {children}
      </main>
  );
}