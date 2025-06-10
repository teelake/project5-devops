
from flask import Flask
app = Flask(__name__)

@app.route('/')
def dashboard():
    return '''
    <html>
        <head>
            <title>CEEYIT Dashboard</title>
           <style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

  body {
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    background: #f0f4f8;
    color: #264653;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 60px 20px;
    min-height: 100vh;
  }

  h1 {
    color: #2a9d8f;
    font-weight: 700;
    font-size: 2.8rem;
    margin-bottom: 8px;
  }

  p {
    font-size: 1.2rem;
    color: #2f3e46;
    margin-bottom: 40px;
  }

  .metrics-container {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 900px;
  }

  .metric-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(42, 157, 143, 0.2);
    padding: 30px 25px;
    width: 220px;
    text-align: center;
    transition: transform 0.3s ease;
  }
  .metric-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 20px rgba(42, 157, 143, 0.35);
  }

  .icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 20px auto;
  }

  /* Animations for SVG icons */
  .animate-path {
    stroke-dasharray: 300;
    stroke-dashoffset: 300;
    animation: draw 2s forwards;
  }

  .animate-circle {
    stroke-dasharray: 188;
    stroke-dashoffset: 188;
    animation: draw 2s forwards;
  }

  @keyframes draw {
    to {
      stroke-dashoffset: 0;
    }
  }

  .metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: #264653;
  }

  .metric-label {
    font-size: 1.1rem;
    margin-top: 6px;
    color: #2a9d8f;
  }
</style>
</head>
<body>

  <h1>CEEYIT Monitoring Dashboard</h1>
  <p>Your DevOps metrics visualized in real-time.</p>

  <div class="metrics-container">

    <div class="metric-card" aria-label="Deployments per day">
      <svg class="icon" viewBox="0 0 64 64" fill="none" stroke="#2a9d8f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" >
        <path class="animate-path" d="M32 12 L32 52 M20 40 L32 52 L44 40" />
        <rect x="12" y="20" width="40" height="20" rx="4" ry="4" />
      </svg>
      <div class="metric-value">18</div>
      <div class="metric-label">Deployments / Day</div>
    </div>

    <div class="metric-card" aria-label="Uptime percentage">
      <svg class="icon" viewBox="0 0 64 64" fill="none" stroke="#2a9d8f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <circle class="animate-circle" cx="32" cy="32" r="30"/>
        <path class="animate-path" d="M32 2 A30 30 0 0 1 62 32" />
        <circle cx="32" cy="32" r="8" fill="#2a9d8f" />
      </svg>
      <div class="metric-value">99.97%</div>
      <div class="metric-label">Uptime</div>
    </div>

    <div class="metric-card" aria-label="Average response time">
      <svg class="icon" viewBox="0 0 64 64" fill="none" stroke="#2a9d8f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <circle class="animate-circle" cx="32" cy="32" r="28"/>
        <path class="animate-path" d="M32 32 L32 14 M32 32 L46 38" />
      </svg>
      <div class="metric-value">250ms</div>
      <div class="metric-label">Avg Response</div>
    </div>

    <div class="metric-card" aria-label="Error rate percentage">
      <svg class="icon" viewBox="0 0 64 64" fill="none" stroke="#e76f51" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <path class="animate-path" d="M16 16 L48 48 M48 16 L16 48" />
        <circle cx="32" cy="32" r="28" stroke="#e76f51" />
      </svg>
      <div class="metric-value">0.12%</div>
      <div class="metric-label">Error Rate</div>
    </div>

  </div>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
