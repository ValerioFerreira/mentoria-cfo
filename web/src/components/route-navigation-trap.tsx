"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export function RouteNavigationTrap({ targetUrl }: { targetUrl: string }) {
  const router = useRouter();

  useEffect(() => {
    // Insere uma entrada no histórico do navegador se o topo atual não for essa marca
    window.history.pushState({ trap: targetUrl }, "", window.location.href);

    const handlePopState = (e: PopStateEvent) => {
      // Quando o usuário clica em 'Voltar', força ir para a página mãe definida
      e.preventDefault();
      router.replace(targetUrl);
    };

    window.addEventListener("popstate", handlePopState);
    return () => {
      window.removeEventListener("popstate", handlePopState);
    };
  }, [router, targetUrl]);

  return null;
}
