import { z } from "zod";

/**
 * Shared zod schemas untuk validasi frontend/backend
 */

// Tipe user publik kecil
export const UserPublicSchema = z.object({
  id: z.string(),
  email: z.string().email(),
  displayName: z.string().nullable(),
  balance: z.number().min(0),
});

export type UserPublic = z.infer<typeof UserPublicSchema>;

// Permintaan penarikan dari frontend
export const WithdrawalRequestSchema = z.object({
  amount: z.number().min(1000), // minimal rupiah, sesuaikan
  currency: z.string().default("IDR"),
  ewalletProvider: z.enum(["OVO", "DANA", "GOPAY", "LINKAJA", "BANK"]),
  destinationAccount: z.string().min(3),
  description: z.string().max(255).optional(),
});

export type WithdrawalRequest = z.infer<typeof WithdrawalRequestSchema>;

// Response transaksi/withdrawal
export const WithdrawalResponseSchema = z.object({
  id: z.string(),
  status: z.enum(["pending", "processing", "completed", "failed"]),
  amount: z.number(),
  currency: z.string(),
  createdAt: z.string(),
  updatedAt: z.string(),
});

export type WithdrawalResponse = z.infer<typeof WithdrawalResponseSchema>;

// Ad reward claim
export const AdRewardClaimSchema = z.object({
  adUnitId: z.string(),
  adInstanceId: z.string().optional(),
  rewardAmount: z.number().min(0),
});

export type AdRewardClaim = z.infer<typeof AdRewardClaimSchema>;