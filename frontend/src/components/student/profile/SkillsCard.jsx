import {
  Code2,
  Database,
  Brain,
  BarChart3,
  Globe,
} from "lucide-react";

export default function SkillsCard({ student }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>
          <h2 className="text-xl font-bold text-gray-900">
            Skills
          </h2>

          <p className="text-sm text-gray-500">
            Technical competencies
          </p>

        </div>

        <div className="rounded-xl bg-red-50 p-3">
          <Code2 className="text-[#8E1528]" size={24} />
        </div>

      </div>

      <div className="space-y-5">

        <Skill
          icon={<Code2 size={18} />}
          title="Programming"
          skills={["Python", "Java", "JavaScript"]}
        />

        <Skill
          icon={<Database size={18} />}
          title="Database"
          skills={["SQL", "PostgreSQL", "MongoDB"]}
        />

        <Skill
          icon={<Brain size={18} />}
          title="AI / Data Science"
          skills={[
            "Machine Learning",
            "Pandas",
            "NumPy",
            "Scikit-learn",
          ]}
        />

        <Skill
          icon={<BarChart3 size={18} />}
          title="Analytics"
          skills={[
            "Power BI",
            "Excel",
            "Data Visualization",
          ]}
        />

        <Skill
          icon={<Globe size={18} />}
          title="Web Development"
          skills={[
            "React",
            "FastAPI",
            "Tailwind CSS",
            "Git",
          ]}
        />

      </div>

    </div>
  );
}

function Skill({ icon, title, skills }) {
  return (
    <div>

      <div className="mb-3 flex items-center gap-2 font-semibold text-gray-800">

        <div className="rounded-lg bg-red-50 p-2 text-[#8E1528]">
          {icon}
        </div>

        {title}

      </div>

      <div className="flex flex-wrap gap-2">

        {skills.map((skill) => (
          <span
            key={skill}
            className="rounded-full bg-gray-100 px-3 py-1 text-sm font-medium text-gray-700 transition hover:bg-red-50 hover:text-[#8E1528]"
          >
            {skill}
          </span>
        ))}

      </div>

    </div>
  );
}