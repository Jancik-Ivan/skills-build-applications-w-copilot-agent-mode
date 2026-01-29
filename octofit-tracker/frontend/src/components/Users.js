import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching users:', err);
        setLoading(false);
      });
  }, [endpoint]);

  const openModal = item => {
    setSelected(item);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelected(null);
  };

  if (loading) return (
    <div className="d-flex justify-content-center align-items-center py-5">
      <div className="spinner-border text-primary me-2" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <span className="text-muted">Loading Users...</span>
    </div>
  );

  return (
    <div className="row">
      <div className="col-12">
        <div className="card card-section shadow-sm">
          <div className="card-header bg-light">
            <h2 className="h4 mb-0">
              <i className="bi bi-person-circle text-primary me-2"></i>Users
            </h2>
          </div>
          <div className="card-body">
            {users.length === 0 ? (
              <div className="alert alert-info text-center py-4" role="alert">
                <i className="bi bi-info-circle me-2"></i>
                No users found. Create your first user to get started.
              </div>
            ) : (
              <div className="table-responsive">
                <table className="table table-striped table-hover table-sm">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Username</th>
                      <th scope="col">Email</th>
                      <th scope="col" className="text-end">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="table-group-divider">
                    {users.map((user, idx) => (
                      <tr key={user.id || idx}>
                        <th scope="row">{user.id || idx + 1}</th>
                        <td>
                          <span className="fw-500">{user.username || user.name || '-'}</span>
                        </td>
                        <td>
                          <a href={`mailto:${user.email || user.email_address}`} className="text-decoration-none">
                            {user.email || user.email_address || '-'}
                          </a>
                        </td>
                        <td className="text-end">
                          <button 
                            className="btn btn-sm btn-outline-primary"
                            onClick={() => openModal(user)}
                            title="View user details"
                          >
                            <i className="bi bi-eye me-1"></i>View
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>

      {showModal && selected && (
        <div className="modal fade show d-block modal-custom" tabIndex="-1" role="dialog" style={{backgroundColor: 'rgba(0,0,0,0.5)'}}>
          <div className="modal-dialog modal-dialog-centered modal-dialog-scrollable" role="document">
            <div className="modal-content">
              <div className="modal-header bg-light">
                <h5 className="modal-title">
                  <i className="bi bi-person-circle text-primary me-2"></i>User Details
                </h5>
                <button 
                  type="button" 
                  className="btn-close" 
                  onClick={closeModal} 
                  aria-label="Close"
                />
              </div>
              <div className="modal-body">
                <pre style={{
                  whiteSpace: 'pre-wrap',
                  wordWrap: 'break-word',
                  fontSize: '0.9rem',
                  backgroundColor: '#f8f9fa',
                  padding: '1rem',
                  borderRadius: '0.375rem',
                  border: '1px solid #dee2e6'
                }}>
                  {JSON.stringify(selected, null, 2)}
                </pre>
              </div>
              <div className="modal-footer bg-light">
                <button 
                  className="btn btn-secondary" 
                  onClick={closeModal}
                >
                  <i className="bi bi-x-circle me-1"></i>Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Users;
