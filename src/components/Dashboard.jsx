import Left from "./Left"
import Right from "./Right"

export default function Dashboard() {
  return (
    <div className="flex flex-col lg:flex-row">
      <Left />
      <Right />
    </div>
  )
}
