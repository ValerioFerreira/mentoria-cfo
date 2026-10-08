-- AlterTable
ALTER TABLE "Invite" ADD COLUMN     "makeAdmin" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "Profile" ALTER COLUMN "examDate" SET DEFAULT '2027-02-28';
