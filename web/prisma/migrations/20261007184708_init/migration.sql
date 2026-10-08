-- CreateEnum
CREATE TYPE "Role" AS ENUM ('USER', 'ADMIN');

-- CreateEnum
CREATE TYPE "ExamBlock" AS ENUM ('I', 'II', 'III');

-- CreateEnum
CREATE TYPE "HoursBand" AS ENUM ('LEVE', 'MODERADO', 'AVANCADO');

-- CreateEnum
CREATE TYPE "ForeignLanguage" AS ENUM ('EN', 'ES');

-- CreateEnum
CREATE TYPE "ContentSource" AS ENUM ('ESTRATEGIA', 'LEGAL_PUBLICO');

-- CreateEnum
CREATE TYPE "AulaKind" AS ENUM ('THEORY', 'PRACTICE');

-- CreateEnum
CREATE TYPE "EditalFit" AS ENUM ('YES', 'PARTIAL', 'NO');

-- CreateEnum
CREATE TYPE "GapSeverity" AS ENUM ('HIGH', 'MEDIUM', 'LOW');

-- CreateEnum
CREATE TYPE "ActivityScope" AS ENUM ('AULA', 'FINAL');

-- CreateEnum
CREATE TYPE "ActivityType" AS ENUM ('TEORIA', 'REVISAO', 'FIXACAO', 'QUESTOES');

-- CreateEnum
CREATE TYPE "ActivityStatus" AS ENUM ('PENDING', 'IN_PROGRESS', 'DONE', 'SKIPPED');

-- CreateEnum
CREATE TYPE "WeekKind" AS ENUM ('CONTENT', 'FINAL_REVIEW');

-- CreateEnum
CREATE TYPE "PlanStatus" AS ENUM ('ACTIVE', 'ARCHIVED');

-- CreateEnum
CREATE TYPE "BizuSet" AS ENUM ('TEORIA', 'REVISAO');

-- CreateEnum
CREATE TYPE "QuestionStatus" AS ENUM ('DRAFT', 'APPROVED', 'FLAGGED', 'RETIRED');

-- CreateEnum
CREATE TYPE "TimeSource" AS ENUM ('TIMER', 'MANUAL');

-- CreateEnum
CREATE TYPE "TimerStatus" AS ENUM ('IDLE', 'RUNNING', 'PAUSED');

-- CreateEnum
CREATE TYPE "QuizKind" AS ENUM ('CADERNO', 'SIMULADO_BLOCO');

-- CreateEnum
CREATE TYPE "ReportStatus" AS ENUM ('OPEN', 'RESOLVED', 'DISMISSED');

-- CreateTable
CREATE TABLE "Subject" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "block" "ExamBlock" NOT NULL,
    "examQuestions" INTEGER NOT NULL,
    "languageGroup" TEXT,
    "foreignLanguage" "ForeignLanguage",
    "sortOrder" INTEGER NOT NULL,
    "estrategiaSection" TEXT,
    "materialCompleteness" DOUBLE PRECISION NOT NULL DEFAULT 1,

    CONSTRAINT "Subject_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Aula" (
    "id" TEXT NOT NULL,
    "subjectId" TEXT NOT NULL,
    "number" INTEGER NOT NULL,
    "title" TEXT NOT NULL,
    "shortTitle" TEXT NOT NULL,
    "kind" "AulaKind" NOT NULL DEFAULT 'THEORY',
    "source" "ContentSource" NOT NULL DEFAULT 'ESTRATEGIA',
    "edital" "EditalFit" NOT NULL DEFAULT 'YES',
    "selectable" BOOLEAN NOT NULL DEFAULT true,
    "totalPages" INTEGER NOT NULL,
    "theoryPages" INTEGER NOT NULL,
    "segmentCount" INTEGER NOT NULL,
    "commentedPages" INTEGER NOT NULL DEFAULT 0,
    "listPages" INTEGER NOT NULL DEFAULT 0,
    "commentedRuns" JSONB NOT NULL,
    "practiceLinks" JSONB NOT NULL,
    "printedOffset" INTEGER NOT NULL DEFAULT 0,
    "incidence" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "note" TEXT,

    CONSTRAINT "Aula_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Gap" (
    "id" TEXT NOT NULL,
    "subjectId" TEXT NOT NULL,
    "item" TEXT NOT NULL,
    "evidence" TEXT NOT NULL,
    "severity" "GapSeverity" NOT NULL,
    "remedy" TEXT NOT NULL,

    CONSTRAINT "Gap_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Topic" (
    "id" TEXT NOT NULL,
    "aulaId" TEXT NOT NULL,
    "parentId" TEXT,
    "level" INTEGER NOT NULL,
    "title" TEXT NOT NULL,
    "pdfPage" INTEGER NOT NULL,
    "printedPage" INTEGER,
    "sortOrder" INTEGER NOT NULL,
    "verified" BOOLEAN NOT NULL DEFAULT false,
    "auto" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "Topic_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Segment" (
    "id" TEXT NOT NULL,
    "aulaId" TEXT NOT NULL,
    "sortOrder" INTEGER NOT NULL,
    "startPage" INTEGER NOT NULL,
    "endPage" INTEGER NOT NULL,
    "startPrinted" INTEGER,
    "endPrinted" INTEGER,
    "pages" INTEGER NOT NULL,
    "load" DOUBLE PRECISION NOT NULL,
    "startTopic" TEXT,
    "startsMidTopic" BOOLEAN NOT NULL DEFAULT false,
    "stopBeforeTopic" TEXT,
    "endsMidTopic" BOOLEAN NOT NULL DEFAULT false,
    "endTopic" TEXT,
    "endsTheory" BOOLEAN NOT NULL DEFAULT false,
    "topicsCovered" JSONB NOT NULL,
    "estMinutes" INTEGER NOT NULL DEFAULT 60,

    CONSTRAINT "Segment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Bizu" (
    "id" TEXT NOT NULL,
    "segmentId" TEXT NOT NULL,
    "summary" TEXT NOT NULL,
    "version" INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT "Bizu_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "BizuItem" (
    "id" TEXT NOT NULL,
    "bizuId" TEXT NOT NULL,
    "set" "BizuSet" NOT NULL,
    "statement" TEXT NOT NULL,
    "isTrue" BOOLEAN NOT NULL,
    "explanation" TEXT NOT NULL,
    "sortOrder" INTEGER NOT NULL,

    CONSTRAINT "BizuItem_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Question" (
    "id" TEXT NOT NULL,
    "subjectId" TEXT NOT NULL,
    "aulaId" TEXT NOT NULL,
    "segmentId" TEXT NOT NULL,
    "topicId" TEXT,
    "support" TEXT,
    "statement" TEXT NOT NULL,
    "explanation" TEXT NOT NULL,
    "difficulty" INTEGER NOT NULL DEFAULT 2,
    "pattern" TEXT NOT NULL,
    "pageRef" INTEGER,
    "status" "QuestionStatus" NOT NULL DEFAULT 'DRAFT',
    "batch" TEXT,

    CONSTRAINT "Question_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "QuestionOption" (
    "id" TEXT NOT NULL,
    "questionId" TEXT NOT NULL,
    "label" TEXT NOT NULL,
    "text" TEXT NOT NULL,
    "isCorrect" BOOLEAN NOT NULL,

    CONSTRAINT "QuestionOption_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "name" TEXT,
    "role" "Role" NOT NULL DEFAULT 'USER',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Invite" (
    "id" TEXT NOT NULL,
    "code" TEXT NOT NULL,
    "email" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "usedAt" TIMESTAMP(3),
    "usedByUserId" TEXT,

    CONSTRAINT "Invite_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Profile" (
    "userId" TEXT NOT NULL,
    "examDate" DATE NOT NULL DEFAULT '2027-02-28',
    "hoursBand" "HoursBand",
    "hoursPerWeek" INTEGER,
    "foreignLanguage" "ForeignLanguage",
    "estrategiaUrl" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Profile_pkey" PRIMARY KEY ("userId")
);

-- CreateTable
CREATE TABLE "Plan" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "version" INTEGER NOT NULL DEFAULT 1,
    "status" "PlanStatus" NOT NULL DEFAULT 'ACTIVE',
    "startDate" DATE NOT NULL,
    "examDate" DATE NOT NULL,
    "params" JSONB NOT NULL,
    "coverage" JSONB NOT NULL,
    "warnings" JSONB NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Plan_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PlanSubject" (
    "planId" TEXT NOT NULL,
    "subjectId" TEXT NOT NULL,
    "level" INTEGER NOT NULL,
    "diagnostic" JSONB NOT NULL,

    CONSTRAINT "PlanSubject_pkey" PRIMARY KEY ("planId","subjectId")
);

-- CreateTable
CREATE TABLE "Week" (
    "id" TEXT NOT NULL,
    "planId" TEXT NOT NULL,
    "index" INTEGER NOT NULL,
    "startDate" DATE NOT NULL,
    "targetMinutes" INTEGER NOT NULL,
    "kind" "WeekKind" NOT NULL DEFAULT 'CONTENT',

    CONSTRAINT "Week_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Activity" (
    "id" TEXT NOT NULL,
    "planId" TEXT NOT NULL,
    "weekId" TEXT NOT NULL,
    "sortOrder" INTEGER NOT NULL,
    "type" "ActivityType" NOT NULL,
    "subjectId" TEXT NOT NULL,
    "aulaId" TEXT NOT NULL,
    "plannedMinutes" INTEGER NOT NULL DEFAULT 60,
    "status" "ActivityStatus" NOT NULL DEFAULT 'PENDING',
    "completedAt" TIMESTAMP(3),
    "key" TEXT NOT NULL,
    "scope" "ActivityScope" NOT NULL DEFAULT 'AULA',
    "fixRanges" JSONB,
    "quizQuestions" INTEGER DEFAULT 25,
    "quizLimitSec" INTEGER DEFAULT 3600,
    "quizMixed" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "Activity_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ActivitySegment" (
    "activityId" TEXT NOT NULL,
    "segmentId" TEXT NOT NULL,

    CONSTRAINT "ActivitySegment_pkey" PRIMARY KEY ("activityId","segmentId")
);

-- CreateTable
CREATE TABLE "ActivityRef" (
    "activityId" TEXT NOT NULL,
    "refActivityId" TEXT NOT NULL,

    CONSTRAINT "ActivityRef_pkey" PRIMARY KEY ("activityId","refActivityId")
);

-- CreateTable
CREATE TABLE "TimeLog" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "activityId" TEXT,
    "seconds" INTEGER NOT NULL,
    "startedAt" TIMESTAMP(3) NOT NULL,
    "endedAt" TIMESTAMP(3),
    "source" "TimeSource" NOT NULL,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "TimeLog_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TimerState" (
    "userId" TEXT NOT NULL,
    "activityId" TEXT,
    "status" "TimerStatus" NOT NULL DEFAULT 'IDLE',
    "startedAt" TIMESTAMP(3),
    "accumulatedMs" INTEGER NOT NULL DEFAULT 0,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "TimerState_pkey" PRIMARY KEY ("userId")
);

-- CreateTable
CREATE TABLE "Note" (
    "userId" TEXT NOT NULL,
    "segmentId" TEXT NOT NULL,
    "text" TEXT NOT NULL,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Note_pkey" PRIMARY KEY ("userId","segmentId")
);

-- CreateTable
CREATE TABLE "QuizSession" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "activityId" TEXT,
    "kind" "QuizKind" NOT NULL DEFAULT 'CADERNO',
    "limitSeconds" INTEGER NOT NULL DEFAULT 3600,
    "startedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "finishedAt" TIMESTAMP(3),
    "autoSubmitted" BOOLEAN NOT NULL DEFAULT false,
    "score" INTEGER,
    "total" INTEGER NOT NULL DEFAULT 25,

    CONSTRAINT "QuizSession_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "QuizAnswer" (
    "id" TEXT NOT NULL,
    "sessionId" TEXT NOT NULL,
    "questionId" TEXT NOT NULL,
    "position" INTEGER NOT NULL,
    "chosenLabel" TEXT,
    "isCorrect" BOOLEAN,
    "secondsSpent" INTEGER NOT NULL DEFAULT 0,
    "flagged" BOOLEAN NOT NULL DEFAULT false,
    "answeredAt" TIMESTAMP(3),

    CONSTRAINT "QuizAnswer_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "BizuAnswer" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "bizuItemId" TEXT NOT NULL,
    "activityId" TEXT,
    "answer" BOOLEAN NOT NULL,
    "isCorrect" BOOLEAN NOT NULL,
    "answeredAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "BizuAnswer_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "QuestionReport" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "questionId" TEXT NOT NULL,
    "reason" TEXT NOT NULL,
    "status" "ReportStatus" NOT NULL DEFAULT 'OPEN',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "QuestionReport_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "Aula_subjectId_idx" ON "Aula"("subjectId");

-- CreateIndex
CREATE UNIQUE INDEX "Aula_subjectId_number_key" ON "Aula"("subjectId", "number");

-- CreateIndex
CREATE INDEX "Topic_aulaId_sortOrder_idx" ON "Topic"("aulaId", "sortOrder");

-- CreateIndex
CREATE UNIQUE INDEX "Segment_aulaId_sortOrder_key" ON "Segment"("aulaId", "sortOrder");

-- CreateIndex
CREATE UNIQUE INDEX "Bizu_segmentId_key" ON "Bizu"("segmentId");

-- CreateIndex
CREATE INDEX "BizuItem_bizuId_set_idx" ON "BizuItem"("bizuId", "set");

-- CreateIndex
CREATE INDEX "Question_segmentId_status_idx" ON "Question"("segmentId", "status");

-- CreateIndex
CREATE INDEX "Question_subjectId_status_idx" ON "Question"("subjectId", "status");

-- CreateIndex
CREATE UNIQUE INDEX "QuestionOption_questionId_label_key" ON "QuestionOption"("questionId", "label");

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Invite_code_key" ON "Invite"("code");

-- CreateIndex
CREATE UNIQUE INDEX "Invite_usedByUserId_key" ON "Invite"("usedByUserId");

-- CreateIndex
CREATE INDEX "Plan_userId_status_idx" ON "Plan"("userId", "status");

-- CreateIndex
CREATE UNIQUE INDEX "Week_planId_index_key" ON "Week"("planId", "index");

-- CreateIndex
CREATE INDEX "Activity_weekId_sortOrder_idx" ON "Activity"("weekId", "sortOrder");

-- CreateIndex
CREATE INDEX "Activity_planId_type_status_idx" ON "Activity"("planId", "type", "status");

-- CreateIndex
CREATE UNIQUE INDEX "Activity_planId_key_key" ON "Activity"("planId", "key");

-- CreateIndex
CREATE INDEX "TimeLog_userId_startedAt_idx" ON "TimeLog"("userId", "startedAt");

-- CreateIndex
CREATE INDEX "TimeLog_activityId_idx" ON "TimeLog"("activityId");

-- CreateIndex
CREATE INDEX "QuizSession_userId_startedAt_idx" ON "QuizSession"("userId", "startedAt");

-- CreateIndex
CREATE INDEX "QuizAnswer_questionId_idx" ON "QuizAnswer"("questionId");

-- CreateIndex
CREATE UNIQUE INDEX "QuizAnswer_sessionId_position_key" ON "QuizAnswer"("sessionId", "position");

-- CreateIndex
CREATE INDEX "BizuAnswer_userId_bizuItemId_idx" ON "BizuAnswer"("userId", "bizuItemId");

-- CreateIndex
CREATE INDEX "QuestionReport_questionId_status_idx" ON "QuestionReport"("questionId", "status");

-- AddForeignKey
ALTER TABLE "Aula" ADD CONSTRAINT "Aula_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gap" ADD CONSTRAINT "Gap_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Topic" ADD CONSTRAINT "Topic_aulaId_fkey" FOREIGN KEY ("aulaId") REFERENCES "Aula"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Topic" ADD CONSTRAINT "Topic_parentId_fkey" FOREIGN KEY ("parentId") REFERENCES "Topic"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Segment" ADD CONSTRAINT "Segment_aulaId_fkey" FOREIGN KEY ("aulaId") REFERENCES "Aula"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Bizu" ADD CONSTRAINT "Bizu_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "BizuItem" ADD CONSTRAINT "BizuItem_bizuId_fkey" FOREIGN KEY ("bizuId") REFERENCES "Bizu"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Question" ADD CONSTRAINT "Question_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Question" ADD CONSTRAINT "Question_aulaId_fkey" FOREIGN KEY ("aulaId") REFERENCES "Aula"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Question" ADD CONSTRAINT "Question_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Question" ADD CONSTRAINT "Question_topicId_fkey" FOREIGN KEY ("topicId") REFERENCES "Topic"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuestionOption" ADD CONSTRAINT "QuestionOption_questionId_fkey" FOREIGN KEY ("questionId") REFERENCES "Question"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Invite" ADD CONSTRAINT "Invite_usedByUserId_fkey" FOREIGN KEY ("usedByUserId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Profile" ADD CONSTRAINT "Profile_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Plan" ADD CONSTRAINT "Plan_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PlanSubject" ADD CONSTRAINT "PlanSubject_planId_fkey" FOREIGN KEY ("planId") REFERENCES "Plan"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PlanSubject" ADD CONSTRAINT "PlanSubject_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Week" ADD CONSTRAINT "Week_planId_fkey" FOREIGN KEY ("planId") REFERENCES "Plan"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Activity" ADD CONSTRAINT "Activity_weekId_fkey" FOREIGN KEY ("weekId") REFERENCES "Week"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Activity" ADD CONSTRAINT "Activity_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Activity" ADD CONSTRAINT "Activity_aulaId_fkey" FOREIGN KEY ("aulaId") REFERENCES "Aula"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ActivitySegment" ADD CONSTRAINT "ActivitySegment_activityId_fkey" FOREIGN KEY ("activityId") REFERENCES "Activity"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ActivitySegment" ADD CONSTRAINT "ActivitySegment_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ActivityRef" ADD CONSTRAINT "ActivityRef_activityId_fkey" FOREIGN KEY ("activityId") REFERENCES "Activity"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ActivityRef" ADD CONSTRAINT "ActivityRef_refActivityId_fkey" FOREIGN KEY ("refActivityId") REFERENCES "Activity"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TimeLog" ADD CONSTRAINT "TimeLog_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TimeLog" ADD CONSTRAINT "TimeLog_activityId_fkey" FOREIGN KEY ("activityId") REFERENCES "Activity"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TimerState" ADD CONSTRAINT "TimerState_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Note" ADD CONSTRAINT "Note_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Note" ADD CONSTRAINT "Note_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuizSession" ADD CONSTRAINT "QuizSession_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuizSession" ADD CONSTRAINT "QuizSession_activityId_fkey" FOREIGN KEY ("activityId") REFERENCES "Activity"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuizAnswer" ADD CONSTRAINT "QuizAnswer_sessionId_fkey" FOREIGN KEY ("sessionId") REFERENCES "QuizSession"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuizAnswer" ADD CONSTRAINT "QuizAnswer_questionId_fkey" FOREIGN KEY ("questionId") REFERENCES "Question"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "BizuAnswer" ADD CONSTRAINT "BizuAnswer_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "BizuAnswer" ADD CONSTRAINT "BizuAnswer_bizuItemId_fkey" FOREIGN KEY ("bizuItemId") REFERENCES "BizuItem"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "BizuAnswer" ADD CONSTRAINT "BizuAnswer_activityId_fkey" FOREIGN KEY ("activityId") REFERENCES "Activity"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuestionReport" ADD CONSTRAINT "QuestionReport_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "QuestionReport" ADD CONSTRAINT "QuestionReport_questionId_fkey" FOREIGN KEY ("questionId") REFERENCES "Question"("id") ON DELETE CASCADE ON UPDATE CASCADE;
