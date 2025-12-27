import fs from 'fs/promises';
import path from 'path';

const DB_PATH = path.join(process.cwd(), 'data', 'db.json');

async function ensureDb() {
  try {
    await fs.access(DB_PATH);
  } catch (e) {
    await fs.mkdir(path.dirname(DB_PATH), { recursive: true });
    const seed = {
      users: [
        {
          id: 'user_demo',
          email: 'rahmatfala4@gmail.com',
          displayName: 'Rahmat Fala',
          balance: 100000,
        },
      ],
      withdrawals: [],
      adClaims: []
    };
    await fs.writeFile(DB_PATH, JSON.stringify(seed, null, 2), 'utf-8');
  }
}

export async function readDb() {
  await ensureDb();
  const raw = await fs.readFile(DB_PATH, 'utf-8');
  return JSON.parse(raw);
}

export async function writeDb(db: any) {
  await ensureDb();
  await fs.writeFile(DB_PATH, JSON.stringify(db, null, 2), 'utf-8');
}

export async function getUserByEmail(email: string) {
  const db = await readDb();
  return db.users.find((u: any) => u.email === email) || null;
}

export async function getUserById(id: string) {
  const db = await readDb();
  return db.users.find((u: any) => u.id === id) || null;
}

export async function updateUserBalance(id: string, newBalance: number) {
  const db = await readDb();
  const user = db.users.find((u: any) => u.id === id);
  if (!user) throw new Error('User not found');
  user.balance = newBalance;
  await writeDb(db);
  return user;
}

export async function createWithdrawalRecord(record: any) {
  const db = await readDb();
  db.withdrawals.push(record);
  await writeDb(db);
  return record;
}

export async function addAdClaim(claim: any) {
  const db = await readDb();
  db.adClaims.push(claim);
  await writeDb(db);
  return claim;
}

export async function hasAdClaim(adInstanceId: string) {
  if (!adInstanceId) return false;
  const db = await readDb();
  return db.adClaims.some((c: any) => c.adInstanceId === adInstanceId);
}
