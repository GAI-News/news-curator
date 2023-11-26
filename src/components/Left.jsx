import React from 'react'
import logo from "../assets/logo.png"

export default function Left() {
  return (
    <div className="w-full bg-orange-300 h-screen p-12 flex flex-col justify-between">
      <div className="flex flex-row justify-between">
        <h1 className="text-[48px] text-slate-800 font-bold">goodnews</h1>
        <img src={logo} alt="" />
      </div>
      <div className="">
        <h1 className="text-[88px] font-bold">Chill out.</h1>
        <p className="text-2xl w-[33.3%] font-medium">We will send you curated news, in the tone and style of your choice.</p>
      </div>
      <div>
        <p className="text-xl w-[50%]">Our goal is to provide news that sets you up for the day, instead of knocking you down.</p>
      </div>
    </div>
  )
}
