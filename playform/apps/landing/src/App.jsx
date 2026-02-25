import React, { useEffect, useRef, useState } from 'react'
import './index.css'

// ─── Data ───────────────────────────────────────────────────────────────────
const STATS = [
  { num: '20,000+', label: '누적 매칭 수' },
  { num: '8,500+', label: '누적 회원 수' },
  { num: '91.3%', label: '서비스 만족도' },
  { num: '100%', label: '진지한 이용자' },
]

const HOW_CARDS = [
  {
    num: '01',
    title: '소수정예 밀착관리',
    desc: '담당 매니저 1명이 단 5명만 전담합니다. 단순 프로필 전달이 아닌, 당신의 상황에 맞춘 1:1 전략으로 움직입니다.',
  },
  {
    num: '02',
    title: '데이터 기반 정밀 매칭',
    desc: '20,000+ 누적 매칭 데이터를 바탕으로 연애 가능성이 높은 상대방만 정밀하게 선별해 소개합니다.',
  },
  {
    num: '03',
    title: '실제 만남 100% 보장',
    desc: '약속 확정부터 피드백까지 처음부터 끝까지 매니저가 조율합니다. 간보기 없이 확정되는 소개팅.',
  },
]

const TESTIMONIALS = [
  { name: '37세 개발자', days: '68일 만에 연애시작', text: '남초 회사에서 기회가 없었는데, 제가 대화에서 실수하는 패턴을 찾아줘서 바로 고쳤어요. 2개월 만에 이상형이랑 사귀고 있습니다.' },
  { name: '32세 자영업', days: '30일 만에 연애시작', text: '연애 경험이 없어서 자신이 없었는데, 카톡 말투부터 실전 피드백까지 받으니 여성분들 반응이 달라지더라고요.' },
  { name: '40세 약사', days: '85일 만에 연애시작', text: '어플 2년 써도 안 됐는데 여기는 달랐어요. 저한테 맞는 분들만 소개해줘서 대화 자체가 너무 잘 통했어요.' },
  { name: '35세 공기업', days: '40일 만에 연애시작', text: '5년 만에 다시 연애 시작했어요. 처음엔 반신반의했는데 지금은 주변 친구들한테 다 추천하고 있어요.' },
  { name: '30세 대학원생', days: '44일 만에 연애시작', text: '썸이 매번 흐지부지 끝났는데, 왜 그랬는지 원인을 찾아줬어요. 그 이후론 진행이 너무 자연스러웠어요.' },
  { name: '38세 공무원', days: '39일 만에 연애시작', text: '믿기 어려웠지만 진짜였어요. 매니저님이 제 상황을 보고 딱 맞는 전략을 짜줬고, 39일 만에 좋아하는 분이 생겼어요.' },
]

const FEED_ITEMS = [
  { name: '35세 김*훈님', result: '68일 만에 연애시작', date: '05.16' },
  { name: '31세 홍*학님', result: '30일 만에 연애시작', date: '05.16' },
  { name: '33세 송*훈님', result: '95일 만에 연애시작', date: '05.15' },
  { name: '24세 이*화님', result: '13일 만에 연애시작', date: '05.15' },
  { name: '38세 김*수님', result: '64일 만에 연애시작', date: '05.14' },
  { name: '38세 심*하님', result: '111일 만에 연애시작', date: '05.14' },
  { name: '36세 박*현님', result: '310일 만에 연애시작', date: '05.13' },
]

// ─── Countdown Hook ──────────────────────────────────────────────────────────
function useCountdown(targetDate) {
  const [time, setTime] = useState({ d: 0, h: 0, m: 0, s: 0 })
  useEffect(() => {
    const tick = () => {
      const diff = new Date(targetDate) - new Date()
      if (diff <= 0) return
      setTime({
        d: Math.floor(diff / 86400000),
        h: Math.floor((diff % 86400000) / 3600000),
        m: Math.floor((diff % 3600000) / 60000),
        s: Math.floor((diff % 60000) / 1000),
      })
    }
    tick()
    const id = setInterval(tick, 1000)
    return () => clearInterval(id)
  }, [targetDate])
  return time
}

// ─── Scroll Reveal Hook ───────────────────────────────────────────────────────
function useReveal() {
  useEffect(() => {
    const els = document.querySelectorAll('.reveal')
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target) }
      })
    }, { threshold: 0.15 })
    els.forEach(el => obs.observe(el))
    return () => obs.disconnect()
  }, [])
}

// ─── Counter Animation ────────────────────────────────────────────────────────
function CountUp({ target, suffix = '' }) {
  const [val, setVal] = useState(0)
  const ref = useRef()
  useEffect(() => {
    const obs = new IntersectionObserver(([e]) => {
      if (e.isIntersecting) {
        obs.disconnect()
        const num = parseFloat(target.replace(/[^0-9.]/g, ''))
        const isFloat = target.includes('.')
        let start = 0
        const steps = 60
        const inc = num / steps
        const id = setInterval(() => {
          start = Math.min(start + inc, num)
          setVal(isFloat ? start.toFixed(1) : Math.round(start))
          if (start >= num) clearInterval(id)
        }, 25)
      }
    }, { threshold: 0.5 })
    if (ref.current) obs.observe(ref.current)
    return () => obs.disconnect()
  }, [target])
  return <span ref={ref}>{val}{suffix}</span>
}

// ─── Main Component ───────────────────────────────────────────────────────────
export default function App() {
  const cd = useCountdown('2026-06-30T23:59:59')
  useReveal()

  const pad = n => String(n).padStart(2, '0')

  // Duplicate testimonials for seamless loop
  const allTesti = [...TESTIMONIALS, ...TESTIMONIALS]
  const initials = name => name.slice(-3, -2)

  return (
    <>
      {/* ── HERO ── */}
      <section className="hero" id="top">
        <div className="hero-bg" />

        <div className="badge-top">
          <span className="badge-dot" />
          2026년 6월 한정 오픈 — 선착순 마감
        </div>

        <h1 className="hero-title">
          매칭은 누구나 한다<br />
          <span className="highlight">연애보장</span>이 진짜
        </h1>

        <p className="hero-subtitle">
          Playform 전문 매니저가 1:1로 움직입니다.
          신청자 10명 중 9명이 3개월 안에 연애를 시작합니다.
        </p>

        <div className="stats-row">
          {STATS.map((s, i) => (
            <React.Fragment key={i}>
              <div className="stat-item">
                <div className="stat-num">{s.num}</div>
                <div className="stat-label">{s.label}</div>
              </div>
              {i < STATS.length - 1 && <div className="stat-divider" />}
            </React.Fragment>
          ))}
        </div>

        <div className="hero-cta">
          <a href="#apply" className="btn-primary" id="hero-cta-btn">
            지금 무료 상담 신청하기 →
          </a>
          <a href="#how" className="btn-ghost" id="hero-how-btn">
            어떻게 다른가요?
          </a>
        </div>
      </section>

      {/* ── COUNTDOWN BAR ── */}
      <div className="countdown-bar">
        <div className="countdown-inner">
          <span className="countdown-label">🔥 마감까지</span>
          <div className="countdown-timer">
            <div className="cd-block">
              <div className="cd-num">{pad(cd.d)}</div>
              <div className="cd-unit">일</div>
            </div>
            <span className="cd-sep">:</span>
            <div className="cd-block">
              <div className="cd-num">{pad(cd.h)}</div>
              <div className="cd-unit">시간</div>
            </div>
            <span className="cd-sep">:</span>
            <div className="cd-block">
              <div className="cd-num">{pad(cd.m)}</div>
              <div className="cd-unit">분</div>
            </div>
            <span className="cd-sep">:</span>
            <div className="cd-block">
              <div className="cd-num">{pad(cd.s)}</div>
              <div className="cd-unit">초</div>
            </div>
          </div>
          <span className="countdown-label">선착순 마감 시 조기종료!</span>
        </div>
      </div>

      {/* ── HOW IT WORKS ── */}
      <div id="how">
        <div className="section">
          <h2 className="section-title reveal">어플·결정사와<br />무엇이 다른가요?</h2>
          <p className="section-subtitle reveal">단순 프로필 전달이 아닙니다. 연애가 될 때까지 함께 움직입니다.</p>
          <div className="how-grid">
            {HOW_CARDS.map((c, i) => (
              <div key={i} className="how-card reveal">
                <div className="how-num">{c.num}</div>
                <div className="how-title">{c.title}</div>
                <p className="how-desc">{c.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── SCROLLING TESTIMONIALS ── */}
      <div className="testimonials-wrapper">
        <div className="testimonials-header">
          <h2 className="section-title">🔥 신청자 10명 중 9명은 연애 중</h2>
          <p className="section-subtitle" style={{ marginBottom: 0 }}>
            프로젝트 종료 이전 연애를 성공한 회원님 기준
          </p>
        </div>
        <div className="scroll-track">
          {allTesti.map((t, i) => (
            <div key={i} className="testi-card">
              <div className="testi-header">
                <div className="testi-avatar">{initials(t.name)}</div>
                <div>
                  <div className="testi-name">{t.name}</div>
                  <div className="testi-meta">실제 사용 후기</div>
                </div>
                <div className="testi-badge">✓ {t.days}</div>
              </div>
              <p className="testi-text">{t.text}</p>
            </div>
          ))}
        </div>
      </div>

      {/* ── LIVE FEED ── */}
      <div className="live-feed">
        <h2 className="feed-title reveal">오늘도 끊이지 않는<br />연애 성공 💌 소식</h2>
        <p className="feed-sub reveal">가만히 있으면 아무 일도 일어나지 않습니다.</p>
        <div className="feed-list">
          {FEED_ITEMS.map((f, i) => (
            <div key={i} className="feed-item reveal" style={{ animationDelay: `${i * 0.1}s` }}>
              <span className="feed-new">NEW</span>
              <div className="feed-content">
                <div className="feed-name">{f.name}</div>
                <div className="feed-result">{f.result} 🎉</div>
              </div>
              <span className="feed-date">{f.date}</span>
            </div>
          ))}
        </div>
      </div>

      {/* ── FINAL CTA ── */}
      <section className="final-cta" id="apply">
        <h2 className="reveal">미뤄두던 연애 숙제<br />지금 함께 풀어드릴게요</h2>
        <p className="reveal">연애를 못하면 3개월 무료 연장. 리스크 없이 시작하세요.</p>
        <div className="hero-cta reveal">
          <a href="#top" className="btn-primary" id="final-cta-btn" style={{ padding: '20px 56px', fontSize: '1.15rem' }}>
            무료 상담 지금 신청하기 →
          </a>
        </div>
      </section>
    </>
  )
}
