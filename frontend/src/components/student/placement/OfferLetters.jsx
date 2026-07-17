import {
  FiDownload,
  FiAward,
} from "react-icons/fi";

const offers = [
  {
    company: "TCS",
    role: "Data Analyst",
    package: "₹7 LPA",
    status: "Accepted",
  },
];

export default function OfferLetters() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">

      <div className="mb-6">
        <h2 className="text-3xl font-bold">
          Offer Letters
        </h2>

        <p className="text-gray-500">
          Job Offers Received
        </p>
      </div>

      {offers.map((offer) => (

        <div
          key={offer.company}
          className="rounded-2xl border p-5"
        >

          <div className="flex items-center justify-between">

            <div>

              <div className="flex items-center gap-2">

                <FiAward className="text-yellow-500" />

                <h3 className="text-xl font-semibold">
                  {offer.company}
                </h3>

              </div>

              <p className="text-gray-500">
                {offer.role}
              </p>

              <p className="mt-1 font-semibold text-[#8E1528]">
                {offer.package}
              </p>

            </div>

            <button
onClick={()=>{
    const link=document.createElement("a");

    link.href="/sample-offer-letter.pdf";

    link.download=`${offer.company}-Offer-Letter.pdf`;

    link.click();
}}
className="rounded-xl bg-[#8E1528] px-5 py-3 text-white hover:bg-[#721220]"
>

              <FiDownload />

            </button>

          </div>

        </div>

      ))}

    </div>
  );
}