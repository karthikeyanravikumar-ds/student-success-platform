import {
  ShieldCheck,
  CircleCheck,
} from "lucide-react";

const rules = [
  "Report to the examination hall 30 minutes before the exam.",
  "Carry your Hall Ticket and College ID Card.",
  "Electronic gadgets including mobile phones are prohibited.",
  "Use only blue or black ink pen.",
  "Follow all invigilator instructions during the examination.",
  "Any malpractice may lead to disciplinary action.",
];

export default function ExamRules() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center gap-3">

        <div className="rounded-xl bg-red-50 p-3 text-[#8E1528]">
          <ShieldCheck size={22} />
        </div>

        <div>

          <h2 className="text-2xl font-bold">
            Examination Rules
          </h2>

          <p className="text-gray-500">
            Important Instructions
          </p>

        </div>

      </div>

      <div className="space-y-4">

        {rules.map((rule) => (

          <div
            key={rule}
            className="flex gap-3"
          >

            <CircleCheck
              size={20}
              className="mt-1 text-green-600"
            />

            <p className="text-gray-700">
              {rule}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}