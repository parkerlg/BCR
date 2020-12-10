BEGIN;
--
-- Create model Ethnicity
--
CREATE TABLE "User_ethnicity" ("id" serial NOT NULL PRIMARY KEY, "ethnicity_name" varchar(30) NOT NULL);
--
-- Create model State
--
CREATE TABLE "User_state" ("id" serial NOT NULL PRIMARY KEY, "state_name" varchar(20) NOT NULL, "state_abbrev" varchar(2) NOT NULL);
--
-- Create model Person
--
CREATE TABLE "User_person" ("user_ptr_id" integer NOT NULL PRIMARY KEY, "phone" varchar(10) NOT NULL, "city" varchar(20) NOT NULL, "zip" varchar(5) NOT NULL, "country" varchar(20) NOT NULL, "type" varchar(20) NOT NULL, "bio" varchar(200) NOT NULL, "profile_picture" varchar(100) NOT NULL, "ethnicity_id" integer NOT NULL, "state_id" integer NOT NULL);
--
-- Create model Organization
--
CREATE TABLE "User_organization" ("id" serial NOT NULL PRIMARY KEY, "organization_name" varchar(40) NOT NULL, "city" varchar(20) NOT NULL, "email" varchar(40) NOT NULL, "size" varchar(20) NOT NULL, "sector" varchar(20) NOT NULL, "state_id" integer NOT NULL);
ALTER TABLE "User_person" ADD CONSTRAINT "User_person_user_ptr_id_4e095c8d_fk_auth_user_id" FOREIGN KEY ("user_ptr_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "User_person" ADD CONSTRAINT "User_person_ethnicity_id_d6808d1a_fk_User_ethnicity_id" FOREIGN KEY ("ethnicity_id") REFERENCES "User_ethnicity" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "User_person" ADD CONSTRAINT "User_person_state_id_9b11cf81_fk_User_state_id" FOREIGN KEY ("state_id") REFERENCES "User_state" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "User_person_ethnicity_id_d6808d1a" ON "User_person" ("ethnicity_id");
CREATE INDEX "User_person_state_id_9b11cf81" ON "User_person" ("state_id");
ALTER TABLE "User_organization" ADD CONSTRAINT "User_organization_state_id_8e399107_fk_User_state_id" FOREIGN KEY ("state_id") REFERENCES "User_state" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "User_organization_state_id_8e399107" ON "User_organization" ("state_id");
COMMIT;

BEGIN;
--
-- Create model Applicant
--
CREATE TABLE "User_applicant" ("person_ptr_id" integer NOT NULL PRIMARY KEY, "website" varchar(35) NOT NULL, "skills" varchar(1000) NOT NULL);
--
-- Create model Organization_Admin
--
CREATE TABLE "User_organization_admin" ("person_ptr_id" integer NOT NULL PRIMARY KEY, "title" varchar(20) NOT NULL, "organization_id_id" integer NOT NULL);
ALTER TABLE "User_applicant" ADD CONSTRAINT "User_applicant_person_ptr_id_d77f9d8e_fk_User_pers" FOREIGN KEY ("person_ptr_id") REFERENCES "User_person" ("user_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "User_organization_admin" ADD CONSTRAINT "User_organization_ad_person_ptr_id_b762e820_fk_User_pers" FOREIGN KEY ("person_ptr_id") REFERENCES "User_person" ("user_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "User_organization_admin" ADD CONSTRAINT "User_organization_ad_organization_id_id_a0a2b433_fk_User_orga" FOREIGN KEY ("organization_id_id") REFERENCES "User_organization" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "User_organization_admin_organization_id_id_a0a2b433" ON "User_organization_admin" ("organization_id_id");
COMMIT;

BEGIN;
--
-- Create model Job_Listing
--
CREATE TABLE "Jobs_job_listing" ("id" serial NOT NULL PRIMARY KEY, "city" varchar(30) NOT NULL, "job_title" varchar(40) NOT NULL, "contracts" varchar(30) NOT NULL, "description" varchar(30) NOT NULL, "skills" varchar(30) NOT NULL, "total_skills" integer NOT NULL, "skill_value_rating" integer NOT NULL, "external_app_link" varchar(50) NULL, "org_admin_id_id" integer NOT NULL, "organization_id_id" integer NOT NULL, "state_id_id" integer NOT NULL);
--
-- Create model Job_Offer
--
CREATE TABLE "Jobs_job_offer" ("id" serial NOT NULL PRIMARY KEY, "city" varchar(30) NOT NULL, "job_title" varchar(30) NOT NULL, "contracts" varchar(30) NOT NULL, "matching_skills" integer NOT NULL, "total_skills" integer NOT NULL, "applicant_id_id" integer NOT NULL, "job_listing_id_id" integer NOT NULL, "organization_id_id" integer NOT NULL, "state_id_id" integer NOT NULL);
--
-- Create model Job_Application
--
CREATE TABLE "Jobs_job_application" ("id" serial NOT NULL PRIMARY KEY, "application_name" varchar(30) NOT NULL, "resume" varchar(100) NOT NULL, "citizen" integer NOT NULL, "authorized" integer NOT NULL, "felony" integer NOT NULL, "felony_desc" varchar(30) NOT NULL, "start_date" date NOT NULL, "applicant_id_id" integer NOT NULL, "job_listing_id_id" integer NOT NULL, "orgization_id_id" integer NOT NULL);
ALTER TABLE "Jobs_job_listing" ADD CONSTRAINT "Jobs_job_listing_org_admin_id_id_4ea32d72_fk_User_orga" FOREIGN KEY ("org_admin_id_id") REFERENCES "User_organization_admin" ("person_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_listing" ADD CONSTRAINT "Jobs_job_listing_organization_id_id_8e7d4b47_fk_User_orga" FOREIGN KEY ("organization_id_id") REFERENCES "User_organization" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_listing" ADD CONSTRAINT "Jobs_job_listing_state_id_id_0c3f5fd3_fk_User_state_id" FOREIGN KEY ("state_id_id") REFERENCES "User_state" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Jobs_job_listing_org_admin_id_id_4ea32d72" ON "Jobs_job_listing" ("org_admin_id_id");
CREATE INDEX "Jobs_job_listing_organization_id_id_8e7d4b47" ON "Jobs_job_listing" ("organization_id_id");
CREATE INDEX "Jobs_job_listing_state_id_id_0c3f5fd3" ON "Jobs_job_listing" ("state_id_id");
ALTER TABLE "Jobs_job_offer" ADD CONSTRAINT "Jobs_job_offer_applicant_id_id_273329da_fk_User_appl" FOREIGN KEY ("applicant_id_id") REFERENCES "User_applicant" ("person_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_offer" ADD CONSTRAINT "Jobs_job_offer_job_listing_id_id_62fb1260_fk_Jobs_job_" FOREIGN KEY ("job_listing_id_id") REFERENCES "Jobs_job_listing" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_offer" ADD CONSTRAINT "Jobs_job_offer_organization_id_id_5cea8db6_fk_User_orga" FOREIGN KEY ("organization_id_id") REFERENCES "User_organization" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_offer" ADD CONSTRAINT "Jobs_job_offer_state_id_id_370c63ae_fk_User_state_id" FOREIGN KEY ("state_id_id") REFERENCES "User_state" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Jobs_job_offer_applicant_id_id_273329da" ON "Jobs_job_offer" ("applicant_id_id");
CREATE INDEX "Jobs_job_offer_job_listing_id_id_62fb1260" ON "Jobs_job_offer" ("job_listing_id_id");
CREATE INDEX "Jobs_job_offer_organization_id_id_5cea8db6" ON "Jobs_job_offer" ("organization_id_id");
CREATE INDEX "Jobs_job_offer_state_id_id_370c63ae" ON "Jobs_job_offer" ("state_id_id");
ALTER TABLE "Jobs_job_application" ADD CONSTRAINT "Jobs_job_application_applicant_id_id_4faef9dc_fk_User_appl" FOREIGN KEY ("applicant_id_id") REFERENCES "User_applicant" ("person_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_application" ADD CONSTRAINT "Jobs_job_application_job_listing_id_id_9c173f59_fk_Jobs_job_" FOREIGN KEY ("job_listing_id_id") REFERENCES "Jobs_job_listing" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Jobs_job_application" ADD CONSTRAINT "Jobs_job_application_orgization_id_id_9a9e0081_fk_User_orga" FOREIGN KEY ("orgization_id_id") REFERENCES "User_organization" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Jobs_job_application_applicant_id_id_4faef9dc" ON "Jobs_job_application" ("applicant_id_id");
CREATE INDEX "Jobs_job_application_job_listing_id_id_9c173f59" ON "Jobs_job_application" ("job_listing_id_id");
CREATE INDEX "Jobs_job_application_orgization_id_id_9a9e0081" ON "Jobs_job_application" ("orgization_id_id");
COMMIT;
