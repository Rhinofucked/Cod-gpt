import { useEffect, useState } from 'react'
import axios from 'axios'

export default function AdminPanel() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    axios.get('/api/admin/users').then(res => setUsers(res.data))
  }, [])

  const updateRole = (id: number, role: string) => {
    axios.put(`/api/admin/users/${id}/role`, { role })
      .then(() => alert('Role updated'))
  }

  return (
    <div className="max-w-3xl mx-auto mt-10">
      <h1 className="text-2xl font-bold mb-4">User Management</h1>
      <table className="w-full table-auto border">
        <thead>
          <tr>
            <th className="border px-2">Username</th>
            <th className="border px-2">Role</th>
            <th className="border px-2">Action</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u: any) => (
            <tr key={u.id}>
              <td className="border px-2">{u.username}</td>
              <td className="border px-2">{u.role}</td>
              <td className="border px-2">
                <select value={u.role} onChange={e => updateRole(u.id, e.target.value)} className="input">
                  <option value="admin">admin</option>
                  <option value="moderator">moderator</option>
                  <option value="contestant">contestant</option>
                </select>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
