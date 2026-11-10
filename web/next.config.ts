import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Arquivos lidos em tempo de execução por caminho montado (process.cwd()): sem isto o rastreamento da Vercel pode
  // deixá-los de fora e o material some em silêncio (índice) ou o carimbo falha (fontes).
  outputFileTracingIncludes: {
    "/*": ["content/material/index.json", "content/directive/anchors.json", "src/assets/fonts/*.ttf"],
  },
  turbopack: {
    rules: {
      "*.css": {
        loaders: ["@tailwindcss/turbopack"],
        as: "*.css",
      },
    },
  },
};

export default nextConfig;
