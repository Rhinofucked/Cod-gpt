import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Dashboard() {
  const [tournaments, setTournaments] = useState([])

  useEffect(() => {
    axios.get('/api/tournaments').then(res => setTournaments(res.data))
  }, [])

  return (
    <div className="max-w-xl mx-auto mt-10">
      <h1 className="text-xl font-bold mb-4">Tournaments</h1>
      {tournaments.map((t: any) => (
        <div key={t.id} className="p-4 border rounded mb-2">
          <h2 className="font-semibold">{t.name}</h2>
          <p>{new Date(t.date).toLocaleString()} - Type: {t.type}</p>
        </div>
      ))}
    </div>
  )
}
