"use client";

import { Loader2, Play } from "lucide-react";
import { useState, useTransition } from "react";
import { Alert, Button } from "@/components/ui";
import { startQuiz } from "@/lib/quiz/actions";

export function QuizStart({ activityId, label = "Iniciar caderno" }: { activityId: string; label?: string }) {
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();
  return (
    <div className="space-y-3">
      <Button
        size="lg"
        disabled={pending}
        onClick={() =>
          start(async () => {
            const r = await startQuiz(activityId);
            if (r && "error" in r) setError(r.error);
          })
        }
      >
        {pending ? <Loader2 className="h-5 w-5 animate-spin" aria-hidden /> : <Play className="h-5 w-5 fill-current" aria-hidden />}
        {pending ? "Montando o caderno…" : label}
      </Button>
      {error && <Alert tone="danger">{error}</Alert>}
    </div>
  );
}
