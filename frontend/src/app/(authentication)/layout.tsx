
import { PropsWithChildren } from "react";
import AuthBanner from "@/components/auth-banner";

export default function AuthenticationLayout({ children }: PropsWithChildren) {
  return (
    <section className="flex flex-1">
      <AuthBanner />
      <main className="flex flex-1 w-full items-center justify-center">
        {children}
      </main>
    </section>

  );
}