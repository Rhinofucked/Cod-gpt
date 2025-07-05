import { useState } from 'react'
import axios from 'axios'

export default function Register() {
  const [form, setForm] = useState({ username: '', password: '', discord_id: '' })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    await axios.post('/api/users/register', form)
    alert('Registered! Now login.')
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-12">
      <input name="username" placeholder="Username" className="input" onChange={handleChange} />
      <input name="password" type="password" placeholder="Password" className="input" onChange={handleChange} />
      <input name="discord_id" placeholder="Discord ID (optional)" className="input" onChange={handleChange} />
      <button className="btn w-full mt-4">Register</button>
    </form>
  )
}
