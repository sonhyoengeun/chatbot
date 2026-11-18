


import streamlit as st
import random

# ==========================================
# 1. 페이지 기본 설정
# ==========================================
st.set_page_config(
    page_title="BON VOYAGE FRANCE",
    page_icon="🇫🇷",
    layout="wide"
)

# ==========================================
# 2. 여행 데이터
# ==========================================
CITIES = {
    "파리": {
        "intro": "예술과 낭만, 미식이 공존하는 프랑스의 수도",
        "places": [
            ("에펠탑", "파리를 대표하는 랜드마크"),
            ("루브르 박물관", "세계적인 예술 작품을 만나는 곳"),
            ("오르세 미술관", "인상주의 작품으로 유명한 미술관"),
            ("몽마르트르", "예술가들의 흔적이 남아 있는 언덕"),
            ("개선문", "샹젤리제 거리와 연결되는 역사적 명소"),
            ("노트르담 대성당", "고딕 건축의 대표적인 문화유산"),
            ("뤽상부르 공원", "여유롭게 산책하기 좋은 도심 공원")
        ],
        "food": ["크루아상과 커피", "에스카르고", "프랑스식 양파 수프", "마카롱"],
        "itinerary": [
            ["에펠탑", "트로카데로 광장", "센강 산책", "에펠탑 야경"],
            ["루브르 박물관", "튈르리 정원", "콩코르드 광장", "샹젤리제 거리"],
            ["몽마르트르", "사크레쾨르 대성당", "오르세 미술관", "생제르맹 거리"],
            ["노트르담 대성당", "생트샤펠", "라틴 지구", "뤽상부르 공원"],
            ["베르사유 궁전", "베르사유 정원", "파리 시내 저녁 식사"],
            ["마레 지구", "보주 광장", "현지 카페", "기념품 쇼핑"],
            ["파리 자유 일정", "현지 시장 방문", "센강 주변 산책"]
        ]
    },

    "니스": {
        "intro": "푸른 지중해와 따뜻한 햇살을 즐기는 휴양 도시",
        "places": [
            ("영국인 산책로", "지중해 해변을 따라 이어지는 산책로"),
            ("마세나 광장", "니스의 중심 광장"),
            ("니스 구시가지", "알록달록한 건물과 현지 시장"),
            ("샤토 언덕", "니스 해안의 아름다운 전망"),
            ("살레야 시장", "지역 식재료와 꽃을 만날 수 있는 시장")
        ],
        "food": ["살라드 니수아즈", "소카", "라따뚜이", "프로방스식 해산물"],
        "itinerary": [
            ["영국인 산책로", "니스 해변", "마세나 광장"],
            ["니스 구시가지", "살레야 시장", "샤토 언덕"],
            ["에즈 마을", "모나코 당일 여행"],
            ["니스 해변", "현지 레스토랑", "구시가지 산책"],
            ["생폴드방스", "예술 갤러리", "니스 자유 시간"],
            ["앙티브 구시가지", "지중해 해변", "니스 야경"],
            ["니스 카페 투어", "기념품 쇼핑"]
        ]
    },

    "리옹": {
        "intro": "프랑스 미식 문화와 역사적인 건축물이 매력적인 도시",
        "places": [
            ("푸르비에르 대성당", "리옹 시내를 내려다보는 명소"),
            ("벨쿠르 광장", "유럽에서 손꼽히는 넓은 광장"),
            ("리옹 구시가지", "유네스코 세계유산 지역"),
            ("테트 도르 공원", "자연 속에서 휴식하기 좋은 공간"),
            ("리옹 미술관", "다양한 시대의 예술 작품")
        ],
        "food": ["리옹식 소시지", "퀴넬", "프랄린 타르트", "현지 비스트로 요리"],
        "itinerary": [
            ["벨쿠르 광장", "리옹 구시가지", "생장 대성당"],
            ["푸르비에르 대성당", "로마 극장", "리옹 전망 감상"],
            ["리옹 미술관", "테트 도르 공원", "현지 레스토랑"],
            ["크루아루스 지구", "벽화 거리", "현지 시장"],
            ["리옹 구시가지", "전통 음식 체험"]
        ]
    },

    "스트라스부르": {
        "intro": "프랑스와 독일 문화가 조화를 이루는 동화 같은 도시",
        "places": [
            ("쁘띠 프랑스", "운하와 목조 건물이 아름다운 지역"),
            ("스트라스부르 대성당", "웅장한 고딕 양식의 건축물"),
            ("로앙 궁전", "역사와 예술을 만날 수 있는 장소"),
            ("일 강변", "운하를 따라 산책하기 좋은 곳"),
            ("유럽 의회", "유럽 통합의 상징적인 공간")
        ],
        "food": ["타르트 플랑베", "슈크루트", "쿠겔호프", "알자스식 전통 요리"],
        "itinerary": [
            ["쁘띠 프랑스", "운하 산책", "스트라스부르 대성당"],
            ["로앙 궁전", "대성당 주변", "현지 레스토랑"],
            ["유럽 의회", "일 강변 산책", "알자스 전통 음식"],
            ["현지 시장", "쁘띠 프랑스", "기념품 쇼핑"]
        ]
    },

    "보르도": {
        "intro": "아름다운 건축물과 세계적으로 유명한 와인 문화의 도시",
        "places": [
            ("부르스 광장", "물의 거울로 유명한 광장"),
            ("물의 거울", "건축물의 반영을 즐길 수 있는 명소"),
            ("보르도 대성당", "역사적인 고딕 양식 건축물"),
            ("시테 뒤 뱅", "와인 문화를 체험하는 박물관"),
            ("생트카트린 거리", "쇼핑과 현지 문화를 즐기는 거리")
        ],
        "food": ["카눌레", "오리 콩피", "프랑스식 치즈", "현지 베이커리"],
        "itinerary": [
            ["부르스 광장", "물의 거울", "보르도 강변"],
            ["보르도 대성당", "생트카트린 거리", "현지 카페"],
            ["시테 뒤 뱅", "현지 시장", "도심 산책"],
            ["생테밀리옹 당일 여행", "보르도 시내"]
        ]
    }
}

# ==========================================
# 3. 비밀번호 인증
# ==========================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        "<h1 style='text-align:center;'>🇫🇷 BON VOYAGE FRANCE</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center;'>Discover France, Your Way.</p>",
        unsafe_allow_html=True
    )

    st.write("")
    password = st.text_input(
        "서비스 접속 비밀번호",
        type="password"
    )

    if st.button("여행 시작하기", use_container_width=True):
        if password == "pnumis":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("비밀번호가 올바르지 않습니다.")

    st.stop()

# ==========================================
# 4. 메인 화면
# ==========================================
st.title("🇫🇷 BON VOYAGE FRANCE")
st.subheader("나만의 프랑스 여행을 설계해 보세요!")
st.caption("Discover France, Your Way.")

st.markdown("""
프랑스의 다양한 도시와 문화를 탐험해 보세요.
여행 스타일과 예산에 맞는 맞춤형 여행 계획을 제공합니다.
""")

# 사이드바
with st.sidebar:
    st.title("✈️ 여행 메뉴")
    menu = st.radio(
        "원하는 서비스를 선택하세요.",
        [
            "🏠 홈",
            "🗺️ 여행 일정 만들기",
            "🏛️ 프랑스 도시 가이드",
            "💬 여행 상담 챗봇",
            "🧳 여행 준비 가이드"
        ]
    )

    st.divider()
    st.caption("BON VOYAGE FRANCE")
    st.caption("Your French Journey Starts Here.")

# ==========================================
# 5. 홈 화면
# ==========================================
if menu == "🏠 홈":

    st.header("Bienvenue en France! 🇫🇷")
    st.write("프랑스의 매력적인 여행지를 만나보세요.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("추천 여행 도시", "5개")
    with col2:
        st.metric("여행 테마", "다양한 선택")
    with col3:
        st.metric("맞춤 일정", "1~7일")

    st.divider()
    st.subheader("🌍 추천 여행 도시")

    for city, info in CITIES.items():
        with st.expander(f"📍 {city}"):
            st.write(info["intro"])
            st.write("**대표 관광지**")
            st.write(", ".join(p[0] for p in info["places"][:4]))
            st.write("**대표 음식**")
            st.write(", ".join(info["food"]))

# ==========================================
# 6. 여행 일정 만들기
# ==========================================
elif menu == "🗺️ 여행 일정 만들기":

    st.header("🗺️ 나만의 프랑스 여행 일정")
    st.write("여행 조건을 선택하면 맞춤 일정을 만들어 드립니다.")

    with st.form("travel_form"):

        city = st.selectbox(
            "1. 방문하고 싶은 도시",
            list(CITIES.keys())
        )

        days = st.slider(
            "2. 여행 기간 (일)",
            1, 7, 3
        )

        budget = st.selectbox(
            "3. 1인 기준 하루 예산 (항공권 제외)",
            [
                "€50 이하",
                "€50~100",
                "€100~200",
                "€200 이상"
            ]
        )

        style = st.selectbox(
            "4. 선호하는 여행 스타일",
            [
                "문화·예술",
                "음식·미식",
                "자연·휴양",
                "역사·건축",
                "쇼핑·도시 탐방"
            ]
        )

        companion = st.selectbox(
            "5. 여행 동행자",
            ["혼자", "친구", "연인", "가족"]
        )

        submitted = st.form_submit_button(
            "✨ 나만의 여행 일정 생성하기",
            use_container_width=True
        )

    if submitted:

        info = CITIES[city]

        st.session_state.last_plan = {
            "city": city,
            "days": days,
            "budget": budget,
            "style": style,
            "companion": companion
        }

        st.divider()
        st.success(f"{city} {days}일 여행 일정이 완성되었습니다!")

        st.subheader(f"🇫🇷 {city} 여행 추천")

        st.write(info["intro"])
        st.write(f"**여행 예산:** {budget}")
        st.write(f"**여행 스타일:** {style}")
        st.write(f"**여행 동행자:** {companion}")

        st.divider()

        st.subheader("📅 추천 여행 일정")

        plans = info["itinerary"]

        for i in range(days):
            daily_plan = plans[i % len(plans)]

            with st.expander(
                f"DAY {i+1} | {city} 여행",
                expanded=(i == 0)
            ):
                for j, place in enumerate(daily_plan):
                    st.write(f"{j+1}. {place}")

        st.divider()

        st.subheader("🍽️ 현지 음식 추천")
        for food in info["food"]:
            st.write(f"• {food}")

        st.info(
            "안내: 본 일정은 여행 계획을 위한 추천 예시입니다. "
            "실제 운영시간, 입장료, 교통편은 방문 전에 확인하세요."
        )

# ==========================================
# 7. 프랑스 도시 가이드
# ==========================================
elif menu == "🏛️ 프랑스 도시 가이드":

    st.header("🏛️ 프랑스 도시 탐험")

    city = st.selectbox(
        "궁금한 도시를 선택하세요.",
        list(CITIES.keys())
    )

    info = CITIES[city]

    st.subheader(f"🇫🇷 {city}")
    st.write(info["intro"])

    st.divider()
    st.subheader("📍 주요 관광 명소")

    for name, description in info["places"]:
        st.markdown(f"**{name}**")
        st.write(description)

    st.divider()
    st.subheader("🥐 대표 음식")

    for food in info["food"]:
        st.write(f"• {food}")

# ==========================================
# 8. 여행 상담 챗봇
# ==========================================
elif menu == "💬 여행 상담 챗봇":

    st.header("💬 BON VOYAGE 여행 상담소")

    st.write(
        "프랑스 여행에 대해 궁금한 점을 자유롭게 질문해 보세요!"
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": (
                    "Bonjour! 🇫🇷 반갑습니다! "
                    "저는 프랑스 여행 전문 상담 챗봇입니다. "
                    "어떤 여행을 계획하고 계신가요?"
                )
            }
        ]

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "예: 파리에서 3일 동안 여행하려면?"
    )

    if question:

        st.session_state.chat_history.append(
            {"role": "user", "content": question}
        )

        q = question.lower()

        if any(word in q for word in ["파리", "에펠", "루브르"]):
            answer = (
                "🇫🇷 **파리 여행을 추천합니다!**\n\n"
                "에펠탑, 루브르 박물관, 몽마르트르, "
                "오르세 미술관을 방문해 보세요.\n\n"
                "특히 센강 주변 산책과 파리의 카페 문화도 "
                "놓치지 마세요!"
            )

        elif any(word in q for word in ["니스", "바다", "해변", "휴양"]):
            answer = (
                "🌊 **니스 여행을 추천합니다!**\n\n"
                "영국인 산책로와 니스 구시가지를 방문해 보세요. "
                "시간이 있다면 에즈와 모나코도 추천합니다.\n\n"
                "지중해의 아름다운 풍경을 즐길 수 있습니다."
            )

        elif any(word in q for word in ["리옹", "음식", "미식", "맛집"]):
            answer = (
                "🥐 **리옹은 프랑스 미식의 중심지입니다!**\n\n"
                "리옹 구시가지와 현지 비스트로를 방문해 보세요. "
                "퀴넬과 프랄린 타르트도 추천합니다."
            )

        elif any(word in q for word in ["스트라스부르", "크리스마스"]):
            answer = (
                "🏘️ **스트라스부르를 추천합니다!**\n\n"
                "쁘띠 프랑스와 스트라스부르 대성당은 "
                "꼭 방문해 볼 만한 장소입니다.\n\n"
                "특히 겨울철 크리스마스 마켓으로 유명합니다."
            )

        elif any(word in q for word in ["보르도", "와인"]):
            answer = (
                "🍇 **보르도 여행을 추천합니다!**\n\n"
                "물의 거울과 부르스 광장을 방문해 보세요. "
                "와인 문화에 관심 있다면 시테 뒤 뱅도 좋습니다."
            )

        elif any(word in q for word in ["교통", "지하철", "기차", "이동"]):
            answer = (
                "🚆 **프랑스 교통 이용 팁입니다.**\n\n"
                "도시 간 이동에는 TGV와 일반 열차를, "
                "도시 내부 이동에는 지하철, 트램, 버스를 활용하세요.\n\n"
                "기차는 SNCF Connect에서 노선과 요금을 확인할 수 있습니다."
            )

        elif any(word in q for word in ["예산", "돈", "경비", "비용"]):
            answer = (
                "💶 **프랑스 여행 예산 안내입니다.**\n\n"
                "숙박, 식비, 교통비, 관광지 입장료를 "
                "구분해서 계획하는 것이 좋습니다.\n\n"
                "여행 도시와 숙박 방식에 따라 비용이 크게 달라집니다."
            )

        elif any(word in q for word in ["안전", "소매치기", "주의"]):
            answer = (
                "🛡️ **프랑스 여행 안전 수칙입니다.**\n\n"
                "1. 지하철과 관광지에서 소지품 관리하기\n"
                "2. 가방은 몸 앞쪽에 두기\n"
                "3. 낯선 사람의 접근과 수상한 서명 요청 주의하기\n"
                "4. 여권과 중요 서류 사본 별도 보관하기"
            )

        elif any(word in q for word in ["안녕", "bonjour"]):
            answer = (
                "Bonjour! 😊 프랑스 여행 상담을 시작해 볼까요? "
                "어떤 도시가 궁금하신가요?"
            )

        else:
            answer = (
                "좋은 질문입니다! 🇫🇷\n\n"
                "현재 저는 프랑스 주요 도시, 관광 명소, "
                "음식, 교통, 예산 및 안전 정보를 중심으로 "
                "여행 상담을 제공하고 있습니다.\n\n"
                "조금 더 구체적으로 질문해 주시면 "
                "도움을 드릴게요!"
            )

        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()

    if st.button("대화 초기화"):
        st.session_state.chat_history = []
        st.rerun()

# ==========================================
# 9. 여행 준비 가이드
# ==========================================
elif menu == "🧳 여행 준비 가이드":

    st.header("🧳 프랑스 여행 준비 가이드")

    st.subheader("✈️ 출국 전 체크리스트")

    checklist = [
        "여권 유효기간 확인",
        "항공권 및 숙소 예약 확인",
        "여행자 보험 가입",
        "해외 결제 카드 준비",
        "유로화 환전",
        "휴대전화 로밍 또는 eSIM 준비",
        "여행 일정 및 교통편 확인",
        "필요한 비자 및 입국 요건 확인"
    ]

    for item in checklist:
        st.checkbox(item)

    st.divider()

    st.subheader("🚆 유용한 프랑스 여행 사이트")

    st.markdown(
        "- [SNCF Connect - 프랑스 기차 예약](https://www.sncf-connect.com/)"
    )
    st.markdown(
        "- [Paris 공식 관광 안내](https://parisjetaime.com/eng/)"
    )
    st.markdown(
        "- [프랑스 관광청](https://www.france.fr/en/)"
    )
    st.markdown(
        "- [RATP - 파리 대중교통](https://www.ratp.fr/en)"
    )

    st.divider()

    st.warning(
        "프랑스의 입국 규정, 교통 운행 및 관광지 운영시간은 "
        "변경될 수 있으므로 공식 사이트에서 최신 정보를 확인하세요."
    )

# ==========================================
# 10. 하단 안내
# ==========================================
st.divider()

st.caption(
    "🇫🇷 BON VOYAGE FRANCE | Discover France, Your Way."
)
st.caption(
    "본 서비스는 여행 정보 제공 및 일정 계획을 위한 "
    "프로토타입입니다."
)
