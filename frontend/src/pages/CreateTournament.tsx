import { useState } from 'react'
import axios from 'axios'

export default function CreateTournament() {
  const [form, setForm] = useState({ name: '', date: '', type: 'blind', max_teams: 4, players_per_team: 2 })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    await axios.post('/api/tournaments', form)
    alert('Tournament created!')
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto mt-12 space-y-2">
      <input name="name" placeholder="Tournament Name" className="input" onChange={handleChange} />
      <input name="date" type="datetime-local" className="input" onChange={handleChange} />
      <select name="type" className="input" onChange={handleChange}>
        <option value="blind">Blind</option>
        <option value="double-blind">Double Blind</option>
      </select>
      <input name="max_teams" type="number" className="input" onChange={handleChange} placeholder="Max Teams" />
      <input name="players_per_team" type="number" className="input" onChange={handleChange} placeholder="Players/Team" />
      <button className="btn w-full">Create</button>
    </form>
  )
}
