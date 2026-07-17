const skillGroups = [
  {
    title: "Frontend",
    skills: ["React", "Tailwind CSS"],
  },
  {
    title: "Backend",
    skills: ["FastAPI"],
  },
  {
    title: "Database",
    skills: ["PostgreSQL", "SQL"],
  },
  {
    title: "Programming",
    skills: ["Python"],
  },
  {
    title: "Tools",
    skills: ["Git"],
  },
];

export default function SkillsUsed() {
  return (
    <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm">

      <h2 className="text-2xl font-bold">
        Skills Used
      </h2>

      <div className="mt-6 space-y-6">

        {skillGroups.map((group) => (

          <div key={group.title}>

            <h3 className="mb-3 font-semibold text-gray-700">
              {group.title}
            </h3>

            <div className="flex flex-wrap gap-2">

              {group.skills.map((skill) => (

                <span
                  key={skill}
                  className="rounded-full bg-red-100 px-4 py-2 text-sm text-red-700"
                >
                  {skill}
                </span>

              ))}

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}