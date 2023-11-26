import React from 'react'
import { useState } from "react"

export default function Form() {

  const startingFormData = {
    mode: "",
    tone: "",
    length: "",
    email: ""
  }

  const [formData, setFormData] = useState(startingFormData);

  const handleChange = (e) => {
    e.preventDefault();
    const value = e.target.value;
    const name = e.target.name;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData)
  }

  return (
    <div className="w-full h-screen max-h-screen bg-slate-800 text-gray-300 flex flex-col justify-between">
      <div className="bg-slate-800 mt-[150px]">
        <h1 className="flex justify-center m-auto text-orange-400 text-[64px]">Let's Get Curatin'</h1>
        <span className="flex text-neutral-400 justify-center m-auto text-center text-xl">Get it? It sounds like "creating"?</span>
        <form onSubmit={handleSubmit} className="flex flex-col justify-center m-auto w-[25%] min-w-[300px] mt-[7.5%]">
          <label className="text-[18px] lg:text-[24px] mb-2">I want my news to be..</label>
          <select required className="outline-none text-gray-700 font-medium text-[20px] rounded-sm px-2 py-1" name="mode" value={formData.mode} onChange={handleChange}>
            <option value="neutral">Neutral</option>
            <option value="uplifting">Uplifting</option>
            <option value="neutral">Demoralizing (don't choose this, silly!)</option>
          </select>
          <label className="text-[18px] lg:text-[24px] mt-6 mb-2">and the tone should be..</label>
          <select required className="outline-none text-gray-700 font-medium text-[20px] rounded-sm px-2 py-1" name="tone" value={formData.tone} onChange={handleChange}>
            <option value="simple">Simple</option>
            <option value="casual">Casual</option>
            <option value="academic">Write me an essay, pal</option>
          </select>
          <label className="text-[18px] lg:text-[24px] mt-6 mb-2">I also like..</label>
          <select required className="outline-none text-gray-700 font-medium text-[20px] rounded-sm px-2 py-1" name="length" value={formData.length} onChange={handleChange}>
            <option value="short">Minimum details</option>
            <option value="original">Original to the source</option>
          </select>
          <label className="text-[18px] lg:text-[24px] mt-6 mb-2">and send it to me at..</label>
          <input required className="outline-none text-gray-800 font-medium text-[20px] rounded-sm px-2 py-1" type="email" name="email" value={formData.email} onChange={handleChange} />
          <button className="w-full bg-orange-400 hover:bg-orange-500 mt-6 py-2 rounded-sm text-xl" type="submit">Send me news!</button>
        </form>
      </div>
      <div className="p-[30px] bg-slate-900 w-full flex flex-col md:flex-row justify-between items-center">
        {/* left Footer */}
        <div className="text-[24px]">
          <h1>Seoul Tech Impact</h1>
        </div>
        {/* middle Footer */}
        <div className="m-0 lg:ml-[125px]">
          <a className="p-2 border-transparent rounded-full border-2 hover:border-2 hover:border-gray-200" href="https://github.com/GAI-News/news-curator">GitHub</a>
        </div>
        {/* right Footer */}
        <div>
          <p className="text-[18px] flex flex-wrap max-w-[150px] lg:max-w-full text-right">Made by Beks, Jeremy, Alex, Smiks and William</p>
        </div>
      </div>
    </div>
  )
}
