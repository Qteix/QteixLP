import vkquick as vq
import time
import typing
from config import access_token

app = vq.App(prefixes=['.л '],filter=vq.filters.OnlyMe())




@app.command("пинг", "ping")
async def greeting(ctx: vq.NewMessage):
    delta = abs(round(time.time() - ctx.msg.date.timestamp(), 2))
    await ctx.edit(f"🟢 | QteixLP version 1.0\n___________________________\n💡Ответ через {delta if delta > 0 else 0.0}с.")






@app.command("статус")
async def delta(ctx: vq.NewMessage, user: vq.User):
    status = await ctx.api.status.get(user_id=user.id)
    await ctx.edit(f"Статус пользователя {user:@[fullname]}: {status['text']}")





@app.command("+др")
async def friend(ctx: vq.NewMessage, user: vq.User):
    try:
        method = await ctx.api.friends.add(user_id=user.id)
        await ctx.edit ("✅Выполнение...")
    except vq.APIError[vq.CODE_174_FRIENDS_ADD_YOURSELF]:
        await ctx.edit ( "❌Невозможно добавить в друзья самого себя.")
    if method == 1:
        await ctx.edit( f"✅Заявка в друзья пользователю {user:@[fullname]} отправлена.")
    elif method == 2:
        await ctx.edit(  f"✅Заявка на добавление в друзья от {user:@[fullname]} одобрена.")
    elif method == 4:
        await ctx.edit( "❌Повторная отправка заявки.")



@app.command("-др")
async def friend(ctx: vq.NewMessage, user: vq.User):
    method = await ctx.api.friends.delete(user_id=user.id)
    method1 = method['success']
    await ctx.edit( "✅Выполнение")
    if method1 == 1:
        await ctx.edit(f"✅ {user:@[fullname]} удален из списка друзей.")
    elif method1 == 1:
        await ctx.edit(f"✅Заявка на добавление в друзья {user:@[fullname]} отклонена.")
    elif method1 == 3:
        await ctx.edit(f"✅Заявка на добавление в друзья {user:@[fullname]} отклонена.")

@app.command("дата")
async def resolve_user(user: vq.User):
    registration_date = await vq.get_user_registration_date(user.id)
    formatted_date = registration_date.strftime("%d.%m.%Y")
    return f"Дата регистрации пользователя {user:@[fullname]}: {formatted_date}"

@app.command("+лайк")
async def add_like_the_user_profile(ctx: vq.NewMessage, user: vq.User[typing.Literal["photo_id"]]):
    photo_id = user.fields["photo_id"].split("_")[1]
    photo_id1 = await ctx.api.method(
        "likes.add", type="photo", owner_id=user.id, item_id=photo_id
    )
    await ctx.edit( f"✅Лайк на аватарку пользователя {user:@[fullname]} оформлен! Стало лайков : {photo_id1['likes']}.")

@app.command("-лайк")
async def add_like_the_user_profile(ctx: vq.NewMessage, user: vq.User[typing.Literal["photo_id"]]):
    photo_id = user.fields["photo_id"].split("_")[1]
    photo_id1 = await ctx.api.method(
        "likes.delete", type="photo", owner_id=user.id, item_id=photo_id
    )
    await ctx.edit( f"✅Лайк на аватарку пользователя {user:@[fullname]} убран! Стало лайков : {photo_id1['likes']}.")

@app.command("ид")
async def revolve_user(user: vq.User):
    user_id = (user.id)
    return f"Айди пользователя {user.fullname}: равен {user_id}"


@app.command("влс")
async def send_message(ctx: vq.NewMessage, user: vq.User, * , text: str,):
    await ctx.api.messages.send(
        user_id=user.id,
        random_id=0,
        message=text
    )
    await ctx.edit(f"✅Сообщение с текстом {text}: было отправлено пользователю {user:@[fullname]}")


@app.command("кик")
async def chat(ctx: vq.NewMessage, user: vq.User):
    try:
        method = await ctx.api.messages.removeChatUser(chat_id=ctx.msg.chat_id, user_id=user.id)
        await ctx.edit( "✅Исключение")
        if method == 1:
            await ctx.edit( f"✅Пользователь {user:@[fullname]} исключен из беседы.")
    except vq.APIError[vq.CODE_925_MESSAGES_CHAT_NOT_ADMIN]:
        await ctx.edit( "⚠Нет доступа.")
    except vq.APIError[vq.CODE_935_MESSAGES_CHAT_USER_NOT_IN_CHAT]:
        await ctx.edit( "⚠Пользователя нету в беседе.")
    except vq.APIError[vq.CODE_945_MESSAGES_CHAT_DISABLED]:
        await ctx.edit( "⚠MESSAGES_CHAT_DISABLED")
    except vq.APIError[vq.CODE_946_MESSAGES_CHAT_UNSUPPORTED]:
        await ctx.edit( "⚠MESSAGES_CHAT_UNSUPPORTED")
    except vq.APIError[vq.CODE_15_ACCESS]:
        await ctx.edit( "⚠Нет доступа.")

@app.command("добавить")
async def chat(ctx: vq.NewMessage , user: vq.User):
    try:
        await ctx.api.messages.addChatUser(
            chat_id=ctx.msg.chat_id,
            user_id=user.id
        )
        await ctx.edit(f'✅Добавляю пользователя {user:@[fullname]}')
        if method == 1:
            await ctx.edit(f'✅Пользователь {user:@[fullname]} добавлен.')
    except vq.APIError[vq.CODE_925_MESSAGES_CHAT_NOT_ADMIN]:
        await ctx.edit("⚠You are not admin of this chat")
    except vq.APIError[vq.CODE_932_MESSAGES_GROUP_PEER_ACCESS]:
        await ctx.edit("⚠Your community can't interact with this peer")
    except vq.APIError[vq.CODE_947_MESSAGES_MEMBER_ACCESS_TO_GROUP_DENIED]:
        await ctx.edit("⚠Can't add user to chat, because user has no access to group")
    except vq.APIError[vq.CODE_15_ACCESS]:
        await ctx.edit("⚠Access denied: can't add this user")

@app.command("чат")
async def chat_info(ctx: vq.NewMessage):
    chat_info = await ctx.api.messages.getChat(
        chat_id=ctx.msg.chat_id
    )
    return f"Название чата {chat_info['title']}: количество участников {chat_info['members_count']} "





app.run(*access_token)
