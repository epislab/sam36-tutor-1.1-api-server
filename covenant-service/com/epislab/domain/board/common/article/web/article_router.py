from fastapi import APIRouter
from com.epislab.account.article.web.article_controller import UserController

router = APIRouter()
controller = UserController()

@router.post(path="/article/create")
async def create_article():
    return controller.hello_article()

@router.get(path="/article/detail")
async def get_article_detail():
    return controller.hello_article()


@router.get("/article/list")
async def get_article_list(db=Depends(get_db)):
    print("🎉🎉 get_articles 로 진입함")
    query = "SELECT * FROM member"
    try:
        results = await db.fetch(query)
        print("💯🌈 데이터 조회 결과:", results)
        # JSON 형태로 반환
        return {"articles": [dict(record) for record in results]}
    except Exception as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        return {"error": "데이터 조회 중 오류가 발생했습니다."}
    
@router.put(path="/article/update")
async def update_article():
    return controller.hello_article()

@router.delete(path="/article/delete")
async def delete_article():
    return controller.hello_article()