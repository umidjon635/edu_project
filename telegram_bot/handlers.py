from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from asgiref.sync import sync_to_async

from courses.models import Course, Registration

router = Router()

class RegisterState(StatesGroup):
    full_name = State()
    email = State()
    phone = State()
    course = State()

@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    courses = await sync_to_async(list)(Course.objects.all())
    if not courses:
        await message.answer("Hozircha kurslar mavjud emas.")
        return

    course_list = "\n".join(f"{i+1}. {c.title}" for i, c in enumerate(courses))
    await message.answer(f"Assalomu alaykum! Ro'yxatdan o'tish uchun ismingizni kiriting:")
    await state.set_state(RegisterState.full_name)

    # saqlab qo'yamiz kurslar ro'yxatini holatga
    await state.update_data(courses=courses)

@router.message(RegisterState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Email manzilingizni kiriting:")
    await state.set_state(RegisterState.email)

@router.message(RegisterState.email)
async def email_handler(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Telefon raqamingizni kiriting (masalan, +998901234567):")
    await state.set_state(RegisterState.phone)

@router.message(RegisterState.phone)
async def phone_handler(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    data = await state.get_data()
    courses = data.get("courses")

    course_buttons = "\n".join(f"{i+1}. {c.title}" for i, c in enumerate(courses))
    await message.answer(f"Quyidagi kurslardan birini tanlang raqam orqali:\n{course_buttons}")
    await state.set_state(RegisterState.course)

@router.message(RegisterState.course)
async def course_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    courses = data.get("courses")
    try:
        course_index = int(message.text) - 1
        course = courses[course_index]
    except (ValueError, IndexError):
        await message.answer("Iltimos, kurs raqamini to'g'ri kiriting.")
        return

    await sync_to_async(Registration.objects.create)(
        telegram_id=message.from_user.id,
        full_name=data["full_name"],
        email=data["email"],
        phone=data["phone"],
        course=course
    )

    await message.answer("✅ Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
    await state.clear()
