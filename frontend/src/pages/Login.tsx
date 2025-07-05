import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await axios.post('/api/users/login', { username, password })
    localStorage.setItem('token', res.data.access_token)
    navigate('/dashboard')
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-12">
      <input placeholder="Username" className="input" value={username} onChange={e => setUsername(e.target.value)} />
      <input placeholder="Password" type="password" className="input" value={password} onChange={e => setPassword(e.target.value)} />
      <button className="btn w-full mt-4" type="submit">Login</button>
    </form>
  )
}
